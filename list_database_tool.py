"""
This is ArcGIS Tool set up code for list_database.py

@author: Brian Wilson <bwilson@clatsopcounty.gov>
"""
import pprint
import arcpy
from PySide6 import __version__, QtCore, QtWidgets, QtGui

# This is for development, so that you can edit code while running in ArcGIS Pro.
import importlib

import list_database

from PySide6 import __version__, QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


class List_Databases_tool(object):

    def __init__(self) -> None:
        """Define the tool (tool name is the name of the class)."""
        self.label = "List Databases tool"
        self.description = """List all database information an APRX project file."""
        self.canRunInBackground = False
        self.category = "Clatsop County"
        #self.stylesheet = "" # I don't know how to use this yet.
        
    def getParameterInfo(self) -> list:
        """Define parameter definitions.
Refer to https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/defining-parameters-in-a-python-toolbox.htm
        """       

        # params[0] = APRX file
        aprx_file = arcpy.Parameter(name="aprx_file",
            displayName="ArcGIS Pro Project file",
            datatype=["DEFile",],
            parameterType="Required", # Required|Optional|Derived
            direction="Input", # Input|Output
        )
        # You can set filters here for example
        #input_fc.filter.list = ["Polygon"]
        # You can set a default if you want -- this makes debugging a little easier.
        aprx_file.value = ""
         
        return [aprx_file]

    def isLicensed(self) -> bool:
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters) -> None:
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
#        if parameters[0].altered:
#            datestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#            p,e = os.path.splitext(parameters[0].valueAsText)
#            parameters[2].value =  p + '_' + datestamp + e
        return

    def updateMessages(self, parameters) -> None:
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""

#        if parameters[2].value == 2:
#            parameters[2].setWarningMessage("Sample warning, you set the number to 2.")
        return

    def execute(self, parameters, messages) -> None:
        """This is the code that executes when you click the "Run" button."""
        
        # See http://resources.arcgis.com/en/help/main/10.2/index.html#//018z00000063000000
        aprx_file   = parameters[0].valueAsText

        try:
            aprx = arcpy.mp.ArcGISProject(aprx_file)
        except Exception as e:
            arcpy.AddError("Fail. %s" % e)
 
        results = list_database.list_database_connections(aprx)
        pprint.pprint(results)

        app = QtWidgets.QApplication([])

        widget = MyWidget()
        widget.resize(800, 600)
        widget.show()

        sys.exit(app.exec())

        return

    
# =============================================================================
if __name__ == "__main__":

    class Messenger(object):
        def addMessage(self, message):
            print(message)

    aprx_file = "c:\\Users\\bwilson\\Documents\\source\\basemap\\basemap.aprx"
    #aprx_file = "C:\\Users\\bwilson\\Documents\\ArcGIS\\Projects\\MyProject\\MyProject.aprx"

    ldb_tool = List_Databases_tool()
    params = ldb_tool.getParameterInfo()
    params[0].value = aprx_file
    ldb_tool.execute(params, Messenger())

    print("Done!")

# That's all!

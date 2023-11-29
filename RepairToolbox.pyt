"""
Repair Toolbox (a ".pyt" file)

A collection of one tool to repair broken Esri projects.
Can I still call it a collection? YES

@author: Brian Wilson <bwilson@clatsopcounty.gov>
"""
import arcpy

# This is for development, so that you can edit code while running in ArcGIS Pro.
import importlib
import list_database
importlib.reload(list_database)

# Import all the tool classes that will be included in this toolbox.
from list_database_tool import List_Databases_tool

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of this .pyt file)."""
        self.description = """Repair toolbox"""

        self.label = "Repair Toolbox"
        self.alias = "RepairToolbox"  # no special characters including spaces!
        self.description = """A collection of repair toosls for project files."""

        # List of tool classes associated with this toolbox
        self.tools = [
            List_Databases_tool,
        ]

def list_tools():
    toolbox = Toolbox()
    print("toolbox:", toolbox.label)
    print("description:", toolbox.description)
    print("tools:")
    for t in toolbox.tools:
        tool = t()
        print('  ', tool.label)
        print('   description:', tool.description)
        for param in tool.getParameterInfo():
            print('    ',param.name,':',param.displayName)
        print()


if __name__ == "__main__":
    # Running this as a standalone script lists information about the toolbox and each tool.
    list_tools()

# That's all!

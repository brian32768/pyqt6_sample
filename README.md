# pyqt-sample

I've never coded with pyqt before, so, here is my exploration.

My goal is to build an app for repairing broken APRX files.
APRX files are ArcGIS Pro project files.

## The first step, Python coded UI

I wrote standalone.py and someday I will revisit it. You can run it.

### Set up environment

Install into a conda environment. Frustratingly this fails with a DLL error.
** Don't do this **

   conda create --name=pyside pyside6 
   conda activate pyside

** Do this **

   conda create -n pyqt python=3.9
   conda activate pyqt
   pip install pyqt6 pyqt6-tools pyside6

The file "hello.py" just does the "hello, world" thing.
The file standalone.py" gives a window with a button, press the button and it asks for an .aprx file. That's it.
Getting to this stage basically took me two days of work. Not worth it. :-P

## QT Designer for the UI

I learned enough yesterday coding GUIs in Python that I want to try the QT Designer.

### Installation 

QT Designer is free, QT Design Studio is $300+/**MONTH**. OMG. That's a big jump.
If you go to the QT website and install on Windows and you will end up with
a registered account and the commercial version that is on a 30-day trial.
QT Designer is included in there somewwhere but, it's almost 3GB of space
burned up on your drive for tools that you can't afford to use after you have
gotten used to them in your trial period.

BUT... **if you install from pip, you get only the free version.** YAY! Your call.

The "pyqt6-tools" package gives me the design tool.
There is no version of the tools in Conda at this time.
Note I installed it above with the pyqt environment. But you could do this.

   conda create -n qtdesigner python=3.9
   conda activate qtdesigner
   pip install pyqt6-tools

When I pin the version of python to 3.9 this I get an older version of PyQT (6.4 vs 6.6)
but it works! I am only using this for the QT Designer and
Later on I will try to figure out incantations to get 6.6...

   conda list pyqt
   # packages in environment at C:\Users\bwilson\AppData\Local\ESRI\conda\envs\pyqt:
   #
   # Name                    Version                   Build  Channel
   pyqt6                     6.4.2                    pypi_0    pypi
   pyqt6-plugins             6.4.2.2.3                pypi_0    pypi
   pyqt6-qt6                 6.4.3                    pypi_0    pypi
   pyqt6-sip                 13.6.0                   pypi_0    pypi
   pyqt6-tools               6.4.2.3.3                pypi_0    pypi

### Run the designer

The commands are

   conda activate qtdesigner # if you did not already
   pyqt6-tools designer

This opens the QT Designer in all its open source glory! I built a main window
with a tree view, a list view, and a button in it. It's the XML file called "myfirstui.ui".

### Generate code from UI

I think this won't work with PySide? Only with PyQT??
You can just load the UI file directly, though. Right?? Damn I hate the newbie stage.

After you create a UI file by saving a design, run a command like this

    pyuic6 myfirstui.ui -o myfirstui.py

Now you have a class for UImainWindow in Python and you can load it into an app.
The app is in myapp.py and it shows how to link the UI to your own python code.

You have to keep track of what you named the objects in your UI. I can see
scaling problems if you wanted to write the next PhotoShop this way but that
is not what i am after. Just a simple utility.

## Resources

The PySide place: https://wiki.qt.io/Qt_for_Python

QT Designer manual: https://doc.qt.io/qt-6/qtdesigner-manual.html

Percipio book: "Beginning PyQT: A Hands-on Approach to GUI Programming with PyQT6, Second Edition"

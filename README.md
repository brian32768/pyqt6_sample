# pyqt-test

I've never coded with pyqt before,
so, here is my exploration.

## QT Designer

I learned enough yesterday coding GUIs that I want to try the QT Designer.

QT Designer is free, QT Design Studio is $300+/**MONTH**. OMG. If you
go to the QT website and install on Windows and you will end up with
a registered account and the commercial version that is on a 30-day trial.
QT Designer is supposedly in there somewwhere but, it's almost 3GB of space
burned up on your drive for tools that you can't afford to use.

BUT... **if you install from pip, you get only the free version.** YAY!

The "pyqt6-tools" package gives me the design tool.
There is no version of the tools in Conda at this time.
I had to pin down python to get a version compatible with
the pypi version of pyqt6-tools. I found 3.9 empirically.

   conda create --name=pyqt python=3.9
   conda activate pyqt
   pip install pyqt6-tools

When I do this I get an older version of PyQT (6.4 vs 6.6)
but I am a newbie so I don't care. Just want to be at version 6.
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

   conda activate pyqt # if you did not already
   pyqt6-tools designer

This opens the QT Designer in all its open source glory!

### Generate code

After you create a UI file by saving a design, run a command like this

    pyuic6 myfirstui.ui -o myfirstui.py

## Resources

QT Designer manual: https://doc.qt.io/qt-6/qtdesigner-manual.html

Percipio book: "Beginning PyQT: A Hands-on Approach to GUI Programming with PyQT6, Second Edition"

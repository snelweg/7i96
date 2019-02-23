# 7i96
7i96 Configuration Tool

To install from GitHub (recommended)
``pip3 git+https://github.com/jethornton/7i96.git``

To upgrade from GitHub
``pip3 git+https://github.com/jethornton/7i96.git upgrade``


To clone the repository and install
``git clone https://github.com/jethornton/7i96.git``

Change to the repository
``cd 7i96``

To install from the clone for general use
``pip3 install .``


For Developers only
To install from the clone and be able to edit
``pip3 install -e .``

To uninstall
``pip3 uninstall 7i96``

To upgrade a cloned repository
``git pull``

To upgrade a regular install
``pip3 install .``

Scope

Read in the ini configuration file for changes.

Create a complete configuration from scratch.

Depends on python3-pyqt5 and python3-setuptools and libpci

``sudo apt-get install python3-pyqt5 libpci-dev``

At this point you can download or clone the tool and run it. If you clone it's
easier to get updates

``git clone https://github.com/jethornton/7i96.git``

Open a terminal in the 7i96 directory and to run

``./7i96.py``

To get updates open a terminal in the 7i96 directory and run

``git pull``

sudo apt-get install python3-setuptools

Open the sample ini file then make changes as needed then build

You can create a configuration then run it with the Axis GUI and use
Machine > Calibration to tune each axis. Save the values to the ini file and
next time you run the 7i96 Configuration Tool it will read the values from the
ini file.

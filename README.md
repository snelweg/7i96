# 7i96
7i96 Configuration Tool

You may need to install pip3 if so open a terminal and do

``sudo apt install python3-pip``

Depends on python3-pyqt5 and python3-setuptools and libpci

``sudo apt-get install python3-pyqt5 libpci-dev``


To install from GitHub (recommended)

``pip3 install git+https://github.com/jethornton/7i96.git``

To upgrade from GitHub

``pip3 install git+https://github.com/jethornton/7i96.git upgrade``


To clone the repository and install

``git clone https://github.com/jethornton/7i96.git``

To get updates to a cloned repository in the 7i96 directory in a terminal do

``git pull``


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

To get updates open a terminal in the 7i96 directory and run

``git pull``

Open the sample ini file then make changes as needed then build

You can create a configuration then run it with the Axis GUI and use
Machine > Calibration to tune each axis. Save the values to the ini file and
next time you run the 7i96 Configuration Tool it will read the values from the
ini file.

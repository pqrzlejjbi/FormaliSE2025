#!/bin/bash

version="2.31.7"

# download and unpack esmini
wget https://github.com/esmini/esmini/archive/refs/tags/v$version.zip
unzip v$version.zip
mv esmini-$version esmini

# build esmini
cd esmini

sudo apt install build-essential gdb ninja-build git pkg-config libgl1-mesa-dev libpthread-stubs0-dev libjpeg-dev libxml2-dev libpng-dev libtiff5-dev libgdal-dev libpoppler-dev libdcmtk-dev libgstreamer1.0-dev libgtk2.0-dev libcairo2-dev libpoppler-glib-dev libxrandr-dev libxinerama-dev curl cmake black

mkdir build
cd build
cmake ..
cmake --build . --config Release --target install

cd ../..

# creating links to resources
ln -s ../esmini/resources/models/e6mini.osgb ./OpenScenarioFiles/e6mini.osgb
ln -s ../esmini/bin/libesminiLib.so ./lib/libesminiLib.so
ln -s ../esmini/bin/libesminiRMLib.so ./lib/libesminiRMLib.so

# setup environment
sudo apt install virtualenv libxkbcommon0
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
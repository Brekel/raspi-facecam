#!/bin/bash

# cleanup previous
rm camera-streamer-*
rm brekel_*
rm *.service
sudo systemctl stop camera-streamer
sudo systemctl stop brekel_LED
sudo systemctl disable camera-streamer
sudo systemctl disable brekel_LED

# update package lists
sudo apt-get update

# download and install camera-streamer software from https://github.com/ayufan/camera-streamer
PACKAGE=camera-streamer-$(test -e /etc/default/raspberrypi-kernel && echo raspi || echo generic)_0.2.8.$(. /etc/os-release; echo $VERSION_CODENAME)_$(dpkg --print-architecture).deb
wget "https://github.com/ayufan/camera-streamer/releases/download/v0.2.8/$PACKAGE"
sudo apt -y install "$PWD/$PACKAGE"

# download and install requirements for neopixel lights
sudo apt-get -y install python3-pip
sudo pip3 install rpi_ws281x
sudo pip3 install adafruit-circuitpython-neopixel

# install service to run automatically at system boot to start camera-streamer and turn lights on
sudo cp camera-streamer.service /etc/systemd/system
sudo cp brekel_LED.service /etc/systemd/system
sudo systemctl enable camera-streamer
sudo systemctl enable brekel_LED
sudo systemctl start camera-streamer
sudo systemctl start brekel_LED

# let the user know that we're done
echo ""
echo ""
echo ""
echo "Finished installing camera-streamer, you can access it through a browser at the following URL:"
echo "http://$(hostname):8080/stream"
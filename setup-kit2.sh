#!/bin/bash -x
#
# Gary Sone - for ClanfielCEP school - see https://twitter.com/HTClanfieldCEP or http://www.clanfield.oxon.sch.uk/
#
# This setup script will create directories, download the PDF worksheets and the Python scripts and set some modprobe parameters
# this file 'wget --content-disposition enos.in/camjamk2'
# wget enos.in/camjamk2 -O- --content-disposition | sh
#
clear
sudo mkdir ~/Documents/EduKitSensors
sudo chown pi:pi ~/Documents/EduKitSensors
cd ~/Documents/EduKitSensors
git clone https://github.com/clanfieldCEP/rpi-camjam.git .

# setup pi for Temperature probe - note: if running Pi2 instructions may be different, also this is a one-time activity.
# see worksheet 3
# device will not show (via 'ls -l') if (duh! - 1/ its not connected & 2/ not wired correctly!
sudo modprobe w1-gpio
sudo modprobe w1-therm
cd /sys/bus/w1/devices
ls -l

# uncomment to install twitter support via twython
# sudo apt-get update && sudo apt-get install python-pip
# sudo pip install twython
## sudo pip install ntplib
## wget https://github.com/soneups/setup-scripts/raw/master/SyncNTP.py

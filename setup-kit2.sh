#!/bin/bash -x
#
# Gary Sone - for ClanfielCEP school - see https://twitter.com/HTClanfieldCEP or http://www.clanfield.oxon.sch.uk/
#
# This setup script will create directories, download the PDF worksheets and the Python scripts and set some modprobe parameters
# wget --content-disposition enos.in/camjamk2
# 
sudo mkdir ~/EduKitSensors
cd ~/EduKitSensors
git clone https://github.com/clanfieldCEP/rpi-camjam.git

# setup pi for Temperature probe - note: if running Pi2 instructions may be different, also this is a one-time activity.
# see worksheet 3
# device will not show (via 'ls -l') if (duh! - 1/ its not connected & 2/ not wired correctly!
sudo modprobe w1-gpio
sudo modprobe w1-therm
cd /sys/bus/w1/devices
ls -l

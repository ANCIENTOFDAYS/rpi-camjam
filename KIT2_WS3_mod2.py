# 3-temperature.py
# Import Libraries
import os
import glob
import time
import sys
import socket

from twython import Twython

os.system('clear')
print sys.argv[0]

# check and warn if not running with root permissions!
if not 'SUDO_UID' in os.environ.keys():
  print 'ERROR: Please re-run as root, hint - sudo'
  sys.exit(1)

# show a useful message on the screen.
print 'Clanfield CE Primary School Twitter Bot - @Pi_Bot_CCEP'

# Initialize the GPIO Pins
os.system('modprobe w1-gpio') # Turns on the GPIO module
os.system('modprobe w1-therm') # Turns on the Temperature module

# Finds the correct device file that holds the temperature data
base_dir = '/sys/bus/w1/devices/' 
device_folder = glob.glob(base_dir + '28*')[0] 
device_file = device_folder + '/w1_slave' 

# A function that reads the sensors data 
def read_temp_raw():
  f = open(device_file, 'r') # Opens the temperature device file 
  lines = f.readlines() # Returns the text 
  f.close()
  return lines

# Convert the value of the sensor into a temperature 
#def read_temp():
lines = read_temp_raw() # Read the temperature 'device file'
  
# While the first line does not contain 'YES', wait for 0.2s
# and then read the device file again. 
while lines[0].strip()[-3:] != 'YES':
  time.sleep(0.2)
  lines = read_temp_raw()
 
# Look for the position of the '=' in the second line of the
# device file.
equals_pos = lines[1].find('t=')
  
# If the '=' is found, convert the rest of the line after the
# '=' into degrees Celsius, then degrees Fahrenheit
if equals_pos != -1:
  temp_string = lines[1][equals_pos+2:]
  temp_c = float(temp_string) / 1000.0
  temp_f = temp_c * 9.0 / 5.0 + 32.0

# Define location of api files - recorded in a file - avoids a GitHub slurp for API keys!
keys_file='/home/pi/Documents/EduKitSensors/twitter_pi_bot_ccep.key'

# Read API keys from file
with open(keys_file) as f:
    CONSUMER_KEY = f.readline().strip("\n")
    CONSUMER_SECRET = f.readline().strip("\n")
    ACCESS_KEY = f.readline().strip("\n")
    ACCESS_SECRET = f.readline().strip("\n")

# Post tweet
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
#api.update_status(status=str(time.strftime("%d/%m/%Y"))+"@"+str(time.strftime("%H:%M:%S"))+' - user: ' + str(wai) + ', host: ' +str(hn)+ ', ip: ' +str(ip)+' ('+sys.argv[1]+')')
#api.update_status(status="@yragstem - my first twitter bot tweet!... #helloworld")
print 'TWEET: '+'On '+str(time.strftime("%d-%b"))+" @ "+str(time.strftime("%H:%M:%S"))+" the temperature reading was "+str(temp_c)+'c, '+str(temp_f)+'f.'
api.update_status(status=str('On '+str(time.strftime("%d-%b"))+" @ "+str(time.strftime("%H:%M:%S"))+" the temperature reading was "+str(temp_c)+'c, '+str(temp_f)+'f.'))

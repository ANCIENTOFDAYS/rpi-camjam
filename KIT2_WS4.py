# Import Libraries
import time
import RPi.GPIO as GPIO

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(Fasle)

# A Variable with the LDR reading pin number
PINLDR = 17

def ReadLDR():
  LDRCount = 0 # sets the count to 0
  GPIO.setup(PINLDR, GPIO.OUT)
  GPIO.output(PINLDR, GPIO.LOW)
  time.sleep(0.1) # Drains all charge from the capcitor

  GPIO.setup(PINLDR, GPIO.IN) # Sets the pin to be an input
  # While the input pin reads 'off' or low, count
  While (GPIO.input(PINLDR) == GPIO.LOW):
    LDRCount += 1 # Add one to the counter
  return LDRCount

While True:
  print ReadLDR()
  time.sleep(1) # Wait for a second
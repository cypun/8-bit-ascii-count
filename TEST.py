from __future__ import print_function
#simple receiver will show status of ports as I am sending.
import time
import RPi.GPIO as GPIO
import os
import binascii

inp = 23





GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
GPIO.setup(inp, GPIO.IN)


if GPIO.input(23) ==1:
	print('switch is on')
else:
	print('switch is off')




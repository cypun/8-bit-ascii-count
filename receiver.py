from __future__ import print_function
#simple receiver will show status of ports as I am sending.
import time
import RPi.GPIO as GPIO
import os
import binascii

inp = [26, 19, 13, 06, 05, 22, 27, 17]
otp = [3, 4]
bin0 = '00000000'




GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
GPIO.setup(inp, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(otp, GPIO.OUT)

GPIO.output(3, True)



try:
	while True:
	
		
			
			
		if GPIO.input(26) == 1:
			bit1 = '1'
		else:
			bit1 = '0'
			
		if GPIO.input(19) == 1:
			bit2 = '1'
		else:
			bit2 = '0'
			
		if GPIO.input(13) == 1:
			bit3 = '1'
		else:
			bit3 = '0'
			
		if GPIO.input(06) == 1:
			bit4 = '1'
		else:
			bit4 = '0'
		
		if GPIO.input(05) == 1:
			bit5 = '1'
		else:
			bit5 = '0'
			
		if GPIO.input(22) == 1:
			bit6 = '1'
		else:
			bit6 = '0'
			
		if GPIO.input(27) == 1:
			bit7 = '1'
		else:
			bit7 = '0'
			
		if GPIO.input(17) == 1:
			bit8 = '1'
		else:
			bit8 = '0'
		
		strbit = bit1 + bit2 + bit3 + bit4 + bit5 + bit6 + bit7 + bit8

		ascdig = int(strbit, base=2)

		txtdata = str(unichr(ascdig))
		
		if txtdata == "\x00":
			txtdata = " "
		if ascdig == 0:
			GPIO.output(3, False)
		else:
			GPIO.output(3, True)
		hexdata = hex(ascdig)
		#with open("fileout.txt", "a") as outFile:
			#outFile.write(txtdata)	
		#print(strbit)
		#print(ascdig)
		
		#print("*****////", txtdata, "\\\\\\\\*****")
		strAry = [txtdata]
		#strAry.append(txtdata)
		time.sleep(.23)
		
		print("      ",txtdata, "     ", hexdata, "     ", strbit, "     ",ascdig)
			
	#time.sleep(.03)
	#os.system('clear
	#time.sleep(.05)

		
finally:
	GPIO.output(3, False)
	GPIO.output(4, False)
	GPIO.cleanup()


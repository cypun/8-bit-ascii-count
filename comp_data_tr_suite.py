import os
import time #allows me to control the time the light operate
	
def sendata():
	#import os
	#import time #allows me to control the time the light operate
	import RPi.GPIO as GPIO # My GPIO Library
	import subprocess

	otp = [26, 19, 13, 06, 05, 22, 27, 17] #These numbers correspond to 
										   #output bits
										   
	sta = [03, 04] #These are my status lights
	###################################################################

	GPIO.setmode(GPIO.BCM) # I use the broadcom mode
	GPIO.setwarnings(False) # I turn off any screen warnings

	GPIO.setup(otp, GPIO.OUT) #These set my bit for output
	GPIO.setup(sta, GPIO.OUT)
	
	GPIO.output(4, True)
	#The lines below that are commented allow for different configurations of
	#what is sent
	# word = raw_input('') accepts typed text and stores it as as string when
	# enter is pressed
	# the line after that makes is just a string of data that is sent directly
	
	#print('Type a word')
	#word = raw_input('')
	
	#word = "This is crazy!!!"
	
	# The 2 lines below look at the output of a process that is kicked off
	#and creates a string from it
	#The next line sets the size of the string, and is used in the for loop
	#so as to determine how many times the process will run for the string
	word = subprocess.check_output('fortune')
	wordLength = len(word)

	try:
	#Here is where the string is converted letter by letter into it's ascii 
	#equivalent, and then sent out of the various GPIO ports
		for outPut in range(0, wordLength):	#notice that the end of the range in 
												#in the for loop is the length of the 
												#string
			
			wordConvert = ord(word[outPut]) 	#this takes each letter in the string I created
												#and converts it into its ascii equivalent
			
			binNum = '{0:b}'.format(wordConvert)	#This converts it into a binary #
			
			GPIO.output(4, True)	#The process of sending data begins

			# Python by default does not do a specific count on the number of bits
			# it only prints bits in use.  The if statements below add the leading
			# zeros to ensure that all of the numbers are 8 bit.

			if len(binNum) == 7:
				binNum = "0" + binNum
			if len(binNum) == 6:
				binNum = "00" + binNum
			if len(binNum) == 5:
				binNum = "000" + binNum
			if len(binNum) == 4:
				binNum = "0000" + binNum
			if len(binNum) == 3:
				binNum = "00000" + binNum
			if len(binNum) == 2:
				binNum = "000000" + binNum
			if len(binNum) == 1:
				binNum = "0000000" + binNum

			print binNum
			# The following if statements test each bit value on wether it is
			# a one or a zero. If the value on the bit is a one it sends a signal
			# to the gpio port. otherwise, it turns that signal off.

			# the one bit
			if binNum[7] == '1':
				GPIO.output(26, True)
			else:
				GPIO.output(26, False)

			# The two bit
			if binNum[6] == '1':
				GPIO.output(19, True)
			else:
				GPIO.output(19, False)

			# The four bit
			if binNum[5] == '1':
				GPIO.output(13, True)
			else:
				GPIO.output(13, False)

			# The 8 bit
			if binNum[4] == '1':
				GPIO.output(06, True)
			else:
				GPIO.output(06, False)

			# the 16 bit
			if binNum[3] == '1':
				GPIO.output(05, True)
			else:
				GPIO.output(05, False)

			# the 32 bit
			if binNum[2] == '1':
				GPIO.output(22, True)
			else:
				GPIO.output(22, False)

			# the 64 bit
			if binNum[1] == '1':
				GPIO.output(27, True)
			else:
				GPIO.output(27, False)

			# The 128 bit
			if binNum[0] == '1':
				GPIO.output(17, True)
			else:
				GPIO.output(17, False)

			
			
			#this line here can be adjusted to ensure that it is not sending to 
			#fast or too slow.
			time.sleep(.22)
			
			os.system('clear')
			# This is the End of the Function,  
		
		#Upon completion of the string of data being spooled out
		#The send lights are all turned off and an a copy of the original message is printed to the screen.
		GPIO.output(otp, False)
		GPIO.output(4, False)
		print('you sent the following in binary to the other machine...')
		print word

		time.sleep(2)
		sendata()
	finally:
		GPIO.output(otp, True)
		time.sleep(2)
		GPIO.output(3, False)
		GPIO.output(4, False)
		GPIO.cleanup()
		recdata()
		
def recdata():
	#from __future__ import print_function
	#simple receiver will show status of ports as I am sending.
	#import time
	import RPi.GPIO as GPIO
	#import os
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
			
			print('      ',txtdata, '     ', hexdata, '     ', strbit, '     ',ascdig)
				
		#time.sleep(.03)
		#os.system('clear
		#time.sleep(.05)

			
	finally:
		GPIO.output(3, False)
		GPIO.output(4, False)
		GPIO.cleanup()
		sendata()

def cleanup():
	import RPi.GPIO as GPIO # My GPIO Library

	otp = [26, 19, 13, 06, 05, 22, 27, 17] #These numbers correspond to 
										   #output bits
										   
	sta = [03, 04] #These are my status lights
	###################################################################

	GPIO.setmode(GPIO.BCM) # I use the broadcom mode
	GPIO.setwarnings(False) # I turn off any screen warnings

	GPIO.setup(otp, GPIO.OUT) #These set my bit for output
	GPIO.setup(sta, GPIO.OUT)
	os.system('clear')
	for turn_off in range(0,1):
		GPIO.output(otp, False)
		GPIO.output(sta, False)
		GPIO.output(otp, False)
	print('')
	print('')
	print('			All data buffers have been cleared')
	time.sleep(3)
	os.system('clear')
	dashboard()
	
	
def splash():
	import os
	import time #allows me to control the time the light operate
	import RPi.GPIO as GPIO # My GPIO Library
	
	print('')
	print('                         ..,co88oc.oo8888cc,..									')
	print('  o8o.               ..,o8889689ooo888o"88888888oooc..							')
	print('.88888             .o888896888".88888888o ?888888888889ooo....					')
	print('a888P          ..c6888969""..,"o888888888o.?8888888888"".ooo8888oo.				')
	print('088P        ..atc88889"".,oo8o.86888888888o 88988889",o888888888888.				')
	print('888t  ...coo688889" .ooo88o88b. 86988988889 8688888 o8888896989^888o				')
	print(' 888888888888"..ooo888968888888  "9o688888  "888988 8888868888 o88888			')
	print('  ""G8889"" ooo888888888888889 .d8o9889""    "8688o."88888988"o888888o .			')
	print('           o8888 """"""""""    o8688"          88868. 888888.68988888"o8o.		')
	print('           88888o.              "8888ooo.         8888. 88888.8898888o"888o.		')
	print('           "888888                "888888            ""8o"8888.8869888oo8888o .	')
	print('      . :.:::::::::::.: .     . :.::::::::.: .   . : ::.:."8888 "888888888888o	')
	print('                                                        :..8888,. "88888888888.	')
	print('                                                        .:o888.o8o.  "866o9888o	')
	print('                 PLATT TECH                              :888.o8888.  "88."89".	')
	print('                                                        . 89  888888    "88":.	')
	print('                    IST                                 :.      8888o			')	
	print('                                                         .       "8888..			')
	print('                  PRESENTS                                         888888o.		')
	print('                                                                    "888889,		')
	print('                                                             . : :.:::::::.: :.	')
	time.sleep(2)
	os.system('clear')
	dashboard()
	
def dashboard():
	print('')
	print('')
	print('          ********************************************')
	for c in range(0,2):
		print('          *                                          *')
	print('          *          Serial Data Transfer            *')
	for c in range(0,2):
		print('          *                                          *')
	print('          *             Platt Tech IST               *')
	for c in range(0,2):
		print('          *                                          *')
	
	print('          ********************************************')
	print('          ********************************************')
	for c in range(0,2):
		print('          *                                          *')
	print('          *    Press 1 to send  data                 *')
	print('          *    Press 2 to receive data               *')
	print('          *    Press 3 to clear all data feeds       *')
	print('          *    Press 4 to quit                       *')
	for c in range(0,2):
		print('          *                                          *')
	print('          ********************************************')
	print('          make an entry')
	print('')
	choice = ''
	while choice != "1" and choice != "2" and choice != "3" and choice != "4": 
		choice = raw_input("          pick 1, 2, 3 or 4 ==> ")
		
		if choice == "1":
			sendata()

		elif choice == "2":
			recdata()

		elif choice == "3":
			cleanup()
	
		elif choice == "4":
			os.system('clear')
			print('  	Goodbye')
			time.sleep(1)
			os.system('clear')
			print('')
			print('')
			print('')
			print('					Goodbye')
			time.sleep(1)
			os.system('clear')			
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('					Goodbye')
			time.sleep(5)
			os.system('clear')




splash()



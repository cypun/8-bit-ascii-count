def main():
	import os
	import time #allows me to control the time the light operate
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
	main()
	
main()



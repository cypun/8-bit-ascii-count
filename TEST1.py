import RPi.GPIO as GPIO







GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

inp = 24 
GPIO.setup(inp, GPIO.OUT)

while True:
	GPIO.output(inp, False)
	
	
	




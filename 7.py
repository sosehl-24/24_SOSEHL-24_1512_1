import argparse
import time
import RPi.GPIO as GPIO

def barva(args):

	#args = parser.parse_args()

	print args

	# LED pin mapping.
	red = 12
	green = 11
	blue = 13

	# GPIO setup.
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	
	GPIO.setup(red, GPIO.OUT)
	GPIO.setup(green, GPIO.OUT)
	GPIO.setup(blue, GPIO.OUT)

	# Set up colors using PWM so we can control individual brightness.
	RED = GPIO.PWM(red, 100)
	GREEN = GPIO.PWM(green, 100)
	BLUE = GPIO.PWM(blue, 100)
	RED.start(0)
	GREEN.start(0)
	BLUE.start(0)

	# Set a color by giving R, G, and B values of 0-255.
	def setColor(rgb = []):
	    # Convert 0-255 range to 0-100.
	    rgb = [(x / 255.0) * 100 for x in rgb]
	    RED.ChangeDutyCycle(rgb[0])
	    GREEN.ChangeDutyCycle(rgb[1])
	    BLUE.ChangeDutyCycle(rgb[2])

	setColor(args)
	time.sleep(3)

while True:
	R= input("Zadaj parametr r (0-255) :")
	G= input("Zadaj parametr g (0-255) :")
	B= input("Zadaj parametr b (0-255) :")

	barva([255-R,255-G,255-B])

GPIO.cleanup()

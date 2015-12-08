import RPi.GPIO as GPIO
import time

#zacatek obrazku
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image


# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Initialize library.
disp.begin(contrast=60)

# Clear display.
disp.clear()
disp.display()

# Load image and convert to 1 bit color.
image = Image.open('VANOCE.pbm').convert('1')

# Display image.
disp.image(image)
disp.display()

#konec obrazku


GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

def mode1():
	for i in range(0,5):
		GPIO.output(5, GPIO.HIGH)
		GPIO.output(6, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(13, GPIO.HIGH)
	        GPIO.output(19, GPIO.HIGH)
	        time.sleep(1)
		GPIO.output(4, GPIO.HIGH)
	        GPIO.output(26, GPIO.HIGH)
	        time.sleep(1)
		GPIO.output(17, GPIO.HIGH)
	        GPIO.output(22, GPIO.HIGH)
	        time.sleep(1)
	        GPIO.output(27, GPIO.HIGH)
	        time.sleep(1)
	        GPIO.output(18, GPIO.HIGH)
	        time.sleep(1)
		 
		GPIO.output(5, GPIO.LOW)
	        GPIO.output(13, GPIO.LOW)
	        GPIO.output(4, GPIO.LOW)
	        GPIO.output(17, GPIO.LOW)
	        GPIO.output(27, GPIO.LOW)
	        GPIO.output(22, GPIO.LOW)
	        GPIO.output(26, GPIO.LOW)
	        GPIO.output(19, GPIO.LOW)
	        GPIO.output(6, GPIO.LOW)
	        GPIO.output(18, GPIO.LOW)
		time.sleep(1)

def mode2():
	cas=0.5
	for i in range(0,5):
		GPIO.output(5,GPIO.HIGH)
		time.sleep(cas)
		GPIO.output(13,GPIO.HIGH)
		time.sleep(cas)
		GPIO.output(4,GPIO.HIGH)
                time.sleep(cas)
		GPIO.output(5,GPIO.LOW)
		GPIO.output(17,GPIO.HIGH)
                time.sleep(cas)
		GPIO.output(13,GPIO.LOW)
                GPIO.output(27,GPIO.HIGH)
                time.sleep(cas)
		GPIO.output(4,GPIO.LOW)
                GPIO.output(22,GPIO.HIGH)
                GPIO.output(18,GPIO.HIGH)
		time.sleep(cas)
                GPIO.output(17,GPIO.LOW)
                GPIO.output(26,GPIO.HIGH)
                GPIO.output(18,GPIO.LOW)
                time.sleep(cas)
		GPIO.output(27,GPIO.LOW)
                GPIO.output(19,GPIO.HIGH)
                time.sleep(cas)
		GPIO.output(22,GPIO.LOW)
                GPIO.output(6,GPIO.HIGH)
                time.sleep(cas)
                GPIO.output(26,GPIO.LOW)
                time.sleep(cas)
                GPIO.output(19,GPIO.LOW)
                time.sleep(cas)
		GPIO.output(6,GPIO.LOW)
                time.sleep(cas)
def mode3():
	cas=0.5
	for i in range(0,5):
		GPIO.output(5, GPIO.HIGH)
		time.sleep(cas)
		GPIO.output(13, GPIO.HIGH)
                time.sleep(cas)
		GPIO.output(4, GPIO.HIGH)
                time.sleep(cas)
                GPIO.output(17, GPIO.HIGH)
                time.sleep(cas)
		GPIO.output(27, GPIO.HIGH)
                time.sleep(cas)
                GPIO.output(18, GPIO.HIGH)
                time.sleep(cas)
                GPIO.output(22, GPIO.HIGH)
                time.sleep(cas)
                GPIO.output(26, GPIO.HIGH)
                time.sleep(cas)
                GPIO.output(19, GPIO.HIGH)
                time.sleep(cas)
                GPIO.output(6, GPIO.HIGH)
                time.sleep(cas)
                GPIO.output(6, GPIO.LOW)
                time.sleep(cas)
                GPIO.output(19, GPIO.LOW)
                time.sleep(cas)
                GPIO.output(26, GPIO.LOW)
                time.sleep(cas)
                GPIO.output(22, GPIO.LOW)
                time.sleep(cas)
                GPIO.output(27, GPIO.LOW)
                time.sleep(cas)
                GPIO.output(18, GPIO.LOW)
                time.sleep(cas)
                GPIO.output(17, GPIO.LOW)
                time.sleep(cas)
                GPIO.output(4, GPIO.LOW)
                time.sleep(cas)
                GPIO.output(13, GPIO.LOW)
                time.sleep(cas)
                GPIO.output(5, GPIO.LOW)
                time.sleep(cas)



try:
	while True:
		pin=input("Zadej sekvenci: ")
	
		if pin == 1:
			mode1()
		elif pin ==2:
			mode2()
		elif pin ==3:
			mode3()
		elif pin==4:
			while True:
				mode1()
				mode2()
				mode3()

except KeyboardInterrupt:
	GPIO.cleanup()
	disp.clear()
	disp.display()
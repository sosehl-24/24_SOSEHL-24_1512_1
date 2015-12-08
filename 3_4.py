def blink():
	for i in range(0,5):
		GPIO.output(15, GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(15, GPIO.LOW)
		time.sleep(0.1)

import RPi.GPIO as GPIO
import time

# nastaveni pinu RPi
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# nastaveni vystupu/vstupu pinu
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.OUT)

# nastaveni promene + "nekonecny" cyklus
svetlo = False

blink()
print "nacteno"

while True:
	# po stisku klavesy sviti 10 sekund
	input_state = GPIO.input(12)
	if input_state == False:
		print("START")
		GPIO.output(15, GPIO.HIGH)
		time.sleep(2)
		GPIO.output(15, GPIO.LOW)
		print("KONEC")
		svetlo=False		

	# stisk rozsviti leddiodu a dalsi stisk ji zhasne
	input_state = GPIO.input(16)
	if input_state == False:
		if svetlo == False:
			GPIO.output(15, GPIO.HIGH)
			svetlo = True
			print("zapnuto")
			time.sleep(0.3)
		else:
			GPIO.output(15, GPIO.LOW)
			svetlo = False
			print("vypnuto")
			time.sleep(0.3)
	
	# po stisku ukonci cyklus
	input_state = GPIO.input(18)
	if input_state == False:
		print "konec programu"
		blink()
		break

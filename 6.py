import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

pwmPin = 15
ledPin = 16
butPin = 18


dc =95

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 50)
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(ledPin, GPIO.LOW)
pwm.start(dc)

print("CTRL + C to exit")

try:
	while 1:
		if GPIO.input(butPin):
			pwm.ChangeDutyCycle(dc)
			GPIO.output(ledPin, GPIO.LOW)
		else:
			for i in xrange(50, 100, 2):
				dc=i
				pwm.ChangeDutyCycle(100-dc)
				GPIO.output(ledPin, GPIO.HIGH)
				time.sleep(0.075)
				GPIO.output(ledPin, GPIO.LOW)
				time.sleep(0.075)
			time.sleep(0.5)
			for i in xrange(0,50,2):
                                dc=100-i
                                pwm.ChangeDutyCycle(100-dc)
                                GPIO.output(ledPin, GPIO.HIGH)
                                time.sleep(0.075)
                                GPIO.output(ledPin, GPIO.LOW)
                                time.sleep(0.075)
except KeyboardInterrupt:
	pwm.stop()
	GPIO.cleanup()

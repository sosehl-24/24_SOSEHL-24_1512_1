import RPi.GPIO as GPIO  
import time

pocet=10

# funkce na blikani  
def blink(pin, pin2):  
        GPIO.output(pin,GPIO.HIGH)
        GPIO.output(pin2,GPIO.LOW)
        time.sleep(0.5)  
        GPIO.output(pin,GPIO.LOW)
        GPIO.output(pin2,GPIO.HIGH)
        time.sleep(0.5)
        return  

# nastaveni pinu RPi  
GPIO.setmode(GPIO.BOARD)  
GPIO.setwarnings(False)

# nastaveni vystupu/vstupu na piny  
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

# for pro blikani 
for i in range(0,pocet):
        print(i+1)
	blink(16, 18)

# vycisteni pinu
GPIO.cleanup()

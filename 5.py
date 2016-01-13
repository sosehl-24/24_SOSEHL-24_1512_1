import RPi.GPIO as GPIO
import time
import urllib2

#nastaveni GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)

#nacteni souboru
file =  urllib2.urlopen("https://ioe.zcu.cz/morse.php?id=hash")
for line in file:
	morse = line

#dotaz na blikani
blik = raw_input("Ches zablikat morseovku? y/n :")

if blik=="y":
# blikani led-diodou
	for i in range(0,len(morse)):
		print morse[i]
		if morse[i] == ".":
			GPIO.output(15, GPIO.HIGH)
			time.sleep(0.5)
			GPIO.output(15, GPIO.LOW)
			time.sleep(0.3)	
		elif morse[i] == "-":
			GPIO.output(15, GPIO.HIGH)
			time.sleep(1)
			GPIO.output(15, GPIO.LOW)
			time.sleep(0.3)
		elif morse[i] == "/":
			time.sleep(1)
		elif morse[i] == " ":
			time.sleep(0.5)
	
pismeno = ""
slovo = ""

#odkodovani morseovky
for i in range(0,len(morse)):
	if morse[i]==" ":
		if pismeno == ".-":
			slovo=slovo+"a"
		elif pismeno == "-...":
			slovo=slovo+"b"
		elif pismeno == "-.-.":
                        slovo=slovo+"c"
		elif pismeno == "-..":
                        slovo=slovo+"d"
                elif pismeno == ".":
                        slovo=slovo+"e"
		elif pismeno == "..-.":
                        slovo=slovo+"f"
                elif pismeno == "--.":
                        slovo=slovo+"g"
                elif pismeno == "....":
                        slovo=slovo+"h"
                elif pismeno == "..":
                        slovo=slovo+"i"
                elif pismeno == ".---":
                        slovo=slovo+"j"
                elif pismeno == "-.-":
                        slovo=slovo+"k"
                elif pismeno == ".-..":
                        slovo=slovo+"l"
                elif pismeno == "--":
                        slovo=slovo+"m"
                elif pismeno == "-.":
                        slovo=slovo+"n"
                elif pismeno == "---":
                        slovo=slovo+"o"
                elif pismeno == ".--.":
                        slovo=slovo+"p"
                elif pismeno == "--.-":
                        slovo=slovo+"q"
                elif pismeno == ".-.":
                        slovo=slovo+"r"
                elif pismeno == "...":
                        slovo=slovo+"s"
                elif pismeno == "-":
                        slovo=slovo+"t"
                elif pismeno == "..-":
                        slovo=slovo+"u"
                elif pismeno == "...-":
                        slovo=slovo+"v"
                elif pismeno == ".--":
                        slovo=slovo+"w"
                elif pismeno == "-..-":
                        slovo=slovo+"x"
                elif pismeno == "-.--":
                        slovo=slovo+"y"
                elif pismeno == "--..":
                        slovo=slovo+"z"
		elif pismeno == "/":
			slovo=slovo+" "
		elif pismeno == ".----":
                        slovo=slovo+"1"
                elif pismeno == "..---":
                        slovo=slovo+"2"
                elif pismeno == "...--":
                        slovo=slovo+"3"
                elif pismeno == "....-":
                        slovo=slovo+"4"
                elif pismeno == ".....":
                        slovo=slovo+"5"
                elif pismeno == "-....":
                        slovo=slovo+"6"
                elif pismeno == "--...":
                        slovo=slovo+"7"
                elif pismeno == "---..":
                        slovo=slovo+"8"
                elif pismeno == "----.":
                        slovo=slovo+"9"
                elif pismeno == "-----":
                        slovo=slovo+"0"
                elif pismeno == "---...":
                        slovo=slovo+":"
                elif pismeno == ".-.-.-":
                        slovo=slovo+"."
                elif pismeno == "-....-":
                        slovo=slovo+"-"

		pismeno = ""
	else:
		pismeno=pismeno+morse[i]







# vypis vysledku
print " "
print "MORSEOVKA : " + morse
print "DEKODOVANO : " + slovo

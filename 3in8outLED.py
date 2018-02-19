import RPi.GPIO as GPIO
import time

###########################################
####VARIABEL DEKLARATION UND DEFINITION####
###########################################


#Alphabet in Binaer (eigene Erfindnung)
ALPHA_REGISTER = {
"0": "00000000",
"A": "00000001", 
"B": "00000010", 
"C": "00000011", 
"D": "00000100", 
"E": "00000101", 
"F": "00000110", 
"G": "00000111",
"H": "00001000",
"I": "00001001",
"J": "00001010",
"K": "00001011",
"L": "00001100",
"M": "00001101",
"N": "00001110",
"O": "00001111",
"P": "00010000",
"Q": "00010001",
"R": "00010010",
"S": "00010011",
"T": "00010100",
"U": "00010101", 
"V": "00010110",
"W": "00010111",
"X": "00011000",
"Y": "00011001",
"Z": "00011010",
}

#globale Variabeln
binOut = []
storePin, shiftPin, dataPin = 15, 14, 18

###########################################
##############FUNKTIONEN###################
###########################################

def stringToBin():
	word = raw_input("Wort zum Umwandeln in Binaer: ")
	word = word.upper()
	
	binArr = []
	iteratorPosition = 0
	
	for x in word:
		binArr.append(ALPHA_REGISTER[x])
		iteratorPosition += 1
		
	return binArr

def bitToLED(arr):
	global storePin, shiftPin, dataPin
	print("Bitliste: ")
	
	for b in arr:
		print(b) 
		GPIO.output(shiftPin, 0)
		GPIO.output(dataPin, int(b))
		GPIO.output(shiftPin, 1)
	
	GPIO.output(storePin, 1)
	
###########################################
##############INITIALISIERUNG##############
###########################################

#GPIO Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(shiftPin, GPIO.OUT) #SH_CP (Taktgeber)
GPIO.setup(storePin, GPIO.OUT) #ST_CP (fuer die Ausgabe an die LEDs)
GPIO.setup(dataPin, GPIO.OUT) #DS (hier die Bits einfliessen lassen)

GPIO.output(14, 0)
GPIO.output(15, 0)
GPIO.output(18, 0)

###########################################
#################PROZESS###################
###########################################

binOut = stringToBin()

for arr in binOut:
	bitToLED(arr)
	time.sleep(1.5)
	GPIO.output(storePin, 0)

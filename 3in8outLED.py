import RPi.GPIO as GPIO
import time

###########################################
####VARIABEL DEKLARATION UND DEFINITION####
###########################################


#Alphabet in Binaer (eigene Erfindung)
ALPHA_REGISTER = {
" ": "00000000",
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
SDI, SRCLK, RCLK = 22, 27, 18
repeat = True

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
		
	binArr.append("00000000")
	
	return binArr

def bitToLED(arr):
	global SDI, SRCLK, RCLK
	#print("Bitliste: ")
	
	for b in arr:
		#print(b) 
		GPIO.output(SDI, int(b))
		GPIO.output(SRCLK, 0)
		GPIO.output(SRCLK, 1)
		

	GPIO.output(RCLK, 0)
	GPIO.output(RCLK, 1)

###########################################
##############INITIALISIERUNG##############
###########################################

#GPIO Pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(SDI, GPIO.OUT) #Datainput, enthaelt die Bits
GPIO.setup(SRCLK, GPIO.OUT) #Schiebt den Bit aus SDI in das Register
GPIO.setup(RCLK, GPIO.OUT) #Laesst das Register einmal ausgeben

GPIO.output(SDI, 0)
GPIO.output(SRCLK, 0)
GPIO.output(RCLK, 0)

###########################################
#################PROZESS###################
###########################################

while repeat:
	bitToLED(["00000000"])	
	binOut = stringToBin()

	for arr in binOut:
		print("Teil Arr: " + arr)
		bitToLED(arr)
		time.sleep(1.5)

	dec = ""
	while dec != "Y" and dec != "N":
		dec = raw_input("Programm abbrechen? Y/N: ")
		if dec == "N":
			repeat = True
		elif dec == "Y":
			repeat = False
		else: 
			print("Bitte Y/N eingeben")
GPIO.cleanup()

#import RPi.GPIO as GPIO
import time

###########################################
####VARIABEL DEKLARATION UND DEFINITION####
###########################################


#Alphabet in Binär (eigene Erfindnung)
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

###########################################
##############FUNKTIONEN###################
###########################################

def stringToBin():
	word = input("Wort zum Umwandeln in Binär: ")
	word = word.upper()
	
	binArr = []
	iteratorPosition = 0
	
	for x in word:
		binArr.append(ALPHA_REGISTER[x])
		iteratorPosition += 1
		
	return binArr

	
###########################################
##############INITIALISIERUNG##############
###########################################

#GPIO Pins
#GPIO.setmode(GPIO.BCM)
#GPIO.setup()
#GPIO.

###########################################
#################PROZESS###################
###########################################

binOut = stringToBin()


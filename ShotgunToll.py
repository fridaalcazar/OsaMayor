import os, sys
from shotgun_api3 import Shotgun 
import os.path
import time

sg = Shotgun("http://upgdl.shotgunstudio.com", "FridaScript", "5130c7f980eae410dc5de8d0e6b3cef0d7067ae83815754636395cc61ee2ea73")

def validateType(userInputType):
	validationType = False 
	while validationType == False:
		if option == 'asset':
			return "Asset"
		elif option == 'shot':
			return "Shot"
		else:
			userInputType = raw_input("ERROR, Invalid data. Try again\nWhat do you want to upload?\n->Asset\n->Shot\n").lower()

def validateID(userInputID):
	validationNumber = False
	while validationNumber == False:
		try:
			userInputID = int(userInputID)
			validationNumber = True
		except:
			userInputID = raw_input("ERROR! The ID must be a number\n")
def validateIDShotgun(validateID):
	shotgunValidation == False
	shotgunFile = sg.find_one(inputType, [["id", "is", validateID]], ["id", "code"])
	#while shotgunValidation == False:
	#	if shotgunFile == None:


option = raw_input("What do you want to upload? \n->Asset\n->Shot\n").lower()
inputType = validateType(option)
ID = raw_input("Type the ID of the %s:" %inputType)
validateID(ID)

print "Data correct"
time.sleep(5)

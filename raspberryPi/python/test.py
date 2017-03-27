#!/usr/bin/env python3
from nanpy import ArduinoApi
from nanpy import Servo
from nanpy import SerialManager
from head import Head
from choreography.crazy_head import CrazyHead
import getch
import time
connection = SerialManager(device='/dev/ttyUSB0')
print("Hello World")
arduino = ArduinoApi(connection=connection)
#for pin in [6,7,8,9,10,11,12,13,14,15]:
#	arduino.pinMode(pin, arduino.OUTPUT)
#	arduino.digitalWrite(pin, arduino.HIGH)
#for pin in [A6,A7,A8,A9,A10,A11,A12,A13,A14,A15]:
head=Head(connection)
crazyhead=CrazyHead(head)
crazyhead.run();
exit()
def switch(argument):
	switcher = {
		'e':lambda: head.moveLeft(),
		's':'ss',
		'd':'dd',
		'f':'ff',	
	}
	return switcher.get(argument)
print("Bitte E,S,D,F eingeben um den Kopf zu bewegen.")
while 1:
	char = getch.getche()
	print(switch(char))
exit()
pin = 16
while(pin <= 17):
	servo = Servo(pin,connection=connection)
	for move in [0, 90, 180, 90, 0]:    
		servo.write(move)
		print("Servo({1}) Position: {0}".format(move,pin))	
		time.sleep(0.5)
	pin+=1

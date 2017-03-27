from nanpy import Servo
class Head(object):
	def __init__(self,connection):
		print("Kopf wird geladen")		
		self.connection=connection		
		self.horizontal=Servo(16)
		self.vertikal=Servo(17)
		self.turningValue=1
		#Justiere Postition
		self.adjustedVertikalPostion=60
		self.adjustedHorizontalPosition=60		
		self.adjust()		
	#Relative Bewegungen	
	def moveLeft(self):
		self.moveHorizontal(self.horizontalPosition + self.turningValue)
	def moveRight(self):
		self.moveHorizontal(self.horizontalPosition - self.turningValue)
	def moveUp(self):
		self.moveVertikal((self.vertikalPosition + self.turningValue))
	def moveDown(self):
		self.moveVertikal(self.vertikalPosition - self.turningValue)
	#Absolute Bewegungen
	def moveHorizontal(self,position):		
		self.angleCheck(position)		
		self.horizontalPosition=position
		self.horizontal.write(position)
	def moveVertikal(self,position):
		self.angleCheck(position)	
		self.vertikalPosition=position
		self.vertikal.write(position)
	def adjust(self):
		self.moveHorizontal(self.adjustedHorizontalPosition)
		self.moveVertikal(self.adjustedVertikalPostion)
	def angleCheck(self,position):		
		if(position>160 or position<0):
			raise RuntimeError("The angel {0} is not valid.".format(position))
	
	

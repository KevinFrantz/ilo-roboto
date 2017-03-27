import time
class CrazyHead(object):
	def __init__(self,head):
		self.head = head
		self.intervall=0.01
	def run(self):

		while(1):
			self.relativ()	
			self.turn()
			self.tilt()	
	def turn(self):
		self.head.adjust()		
		count=0		
		while (count <160 ):
			self.head.moveHorizontal(count)
			time.sleep(self.intervall)
			count += 10;
		while (count >0 ):
			self.head.moveHorizontal(count)
			time.sleep(self.intervall)
			count -= 10;
	def tilt(self):
		self.head.adjust()		
		count=0		
		while (count <160 ):
			self.head.moveVertikal(count)
			time.sleep(self.intervall)
			count += 10;		
		while (count >0 ):
			self.head.moveVertikal(count)
			time.sleep(self.intervall)
			count -= 10;
	def relativ(self):
		self.head.adjust()				
		while (self.head.vertikalPosition <160 and self.head.horizontalPosition <160):						
			self.head.moveUp()
			self.head.moveLeft()
			time.sleep(self.intervall)		
		while (self.head.vertikalPosition > 0 and self.head.horizontalPosition > 0 ):
			self.head.moveDown()
			self.head.moveRight()
			time.sleep(self.intervall)


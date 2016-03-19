
class Coordinate:

	def __init__(self,xCoord,yCoord,value=None):
		self.xCoord = xCoord
		self.yCoord = yCoord
		self.value = value
		self.xPath = [xCoord]
		self.yPath = [yCoord]
		self.zPath = [value]

	def addX(self,x):
		self.xPath.append(x)

	def getXPath(self):
		return self.xPath	

	def addY(self,x):
		self.yPath.append(x)

	def getYPath(self):
		return self.yPath	

	def addZ(self,x):
		self.zPath.append(x)

	def getZPath(self):
		return self.zPath

	def getX(self):
		return self.xCoord

	def getY(self):
		return self.yCoord

	def getValue(self):
		return self.value

	def setX(self,xCoord):
		self.xCoord = xCoord

	def setY(self,yCoord):
		self.yCoord = yCoord

	def setValue(self,value):
		self.value = value

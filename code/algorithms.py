import math
import random
from coordinate import Coordinate

class Algorithms:

	def __init__(self):
		#Flags, used to specify print output

		#Hill flag, prints the output of the hill climbing algorithm
		self.HILL = True

		#Hill progress flag, prints the progress of the hill climbing algorithm
		self.HILL_PROGRESS = False

		#Hill random flag, prints the output of the hill climbing algoritm with random restarts
		self.HILL_RANDOM = True

		#Hill random progress flag, prints the progress of the hill climbing algorithm with random restarts
		self.HILL_RANDOM_PROGRESS = True

		#Simulated annealing flag, prints the output of the simulated annealing algorithm
		self.SA = True

		#Simulated annealing progress flag, prints the progress of the simulated annealing algorithm
		self.SA_PROGRESS = False

		#This wasn't a specified parameter in the SA function for the project, 
		#so here is where you control how slow the temperature drops.
		self.TEMP_DECREASE = 0.001


	def print_flag(self,myStr,FLAG):
		if FLAG == self.HILL_PROGRESS and self.HILL_PROGRESS:
			print(myStr)
		elif FLAG == self.HILL_RANDOM_PROGRESS and self.HILL_RANDOM_PROGRESS:
			print(myStr)
		elif FLAG == self.HILL and self.HILL:
			print(myStr)
		elif FLAG == self.HILL_RANDOM and self.HILL_RANDOM:
			print(myStr)
		elif FLAG == self.SA and self.SA:
			print(myStr)
		elif FLAG == self.SA_PROGRESS and self.SA_PROGRESS:
			print(myStr)

	def temp_function(self,temperature,newVal,oldVal):
		if temperature < 0:
			return False
		ans = 0
		try:
			ans = math.exp((newVal-oldVal)/temperature)
		except OverflowError:
			return False

		prob = random.uniform(0,1)
		return prob < ans

	def simulated_annealing(self,function_to_optimize, step_size, max_temp, xmin, xmax, ymin, ymax, startx=None, starty=None):
		if startx == None:
			startx=xmin
		if starty == None:
			starty=ymin

		currX = startx
		currY = starty
		temp = max_temp
		currValue = function_to_optimize(currX,currY)
		searching = True
		coord = Coordinate(currX,currY,currValue) 

		while searching:
			progressed = False
			searching = False
			xPos = currX + step_size

			#Attempt to increase X by the step
			if xPos <= xmax:
				temp -= self.TEMP_DECREASE
				newVal = function_to_optimize(xPos,currY)
				xTemp = self.temp_function(temp,newVal,currValue)

				if newVal < currValue or xTemp:
					self.print_flag("CLIMBING BY INC. X "+str(xPos),self.SA_PROGRESS)
					if xTemp:
						xPos += step_size
					currValue = newVal
					currX = xPos
					searching = True
					progressed = True


			xNeg = currX - step_size

			#Attempt instead to decrease X by the step
			if xNeg >= xmin:
				temp -= self.TEMP_DECREASE
				newVal = function_to_optimize(xNeg,currY)
				xTemp = self.temp_function(temp,newVal,currValue)

				if newVal < currValue:
					self.print_flag("CLIMBING BY DEC. X "+str(xNeg),self.SA_PROGRESS)
					currValue = newVal
					currX = xNeg
					searching = True
					progressed = True

			yPos = currY + step_size

		
			#Attempt to increase Y by the step
			if yPos <= ymax:
				temp -= self.TEMP_DECREASE
				newVal = function_to_optimize(currX,yPos)
				yTemp = self.temp_function(temp,newVal,currValue)

				if newVal < currValue or yTemp:
					self.print_flag("CLIMBING BY INC. Y",self.SA_PROGRESS)
					if yTemp:
						yPos += step_size
					currValue = newVal
					currY = yPos
					searching = True
					progressed = True

			yNeg = currY - step_size

			#Attempt to decrease Y by the step
			if yNeg >= ymin:	
				temp -= self.TEMP_DECREASE
				newVal = function_to_optimize(currX,yNeg)
				yTemp = self.temp_function(temp,newVal,currValue)
				if newVal < currValue:
					self.print_flag("CLIMBING BY DEC. Y",self.SA_PROGRESS)
					currValue = newVal
					currY = yNeg
					searching = True
					progressed = True

			#If we don't go anywhere, don't add the same coordinates twice
			if progressed:
				coord.addX(currX)
				coord.addY(currY)
				coord.addZ(currValue)

		coord.setX(currX)
		coord.setY(currY)
		coord.setValue(currValue)
		self.print_flag("MIN FOUND X:"+str(currX)+" Y:"+str(currY)+" VALUE:"+str(currValue)+"\n",self.SA)
		return coord

	def hill_climb(self, function_to_optimize,step_size,xmin,xmax,ymin,ymax,startx=None,starty=None):
		if startx == None:
			startx=xmin
		if starty == None:
			starty=ymin

		currX = startx
		currY = starty

		currValue = function_to_optimize(currX,currY)

		coord = Coordinate(currX,currY,currValue) 
		searching = True

		while searching:
			searching = False
			xPos = currX + step_size

			#Attempt to increase X by the step
			if xPos <= xmax:
				newVal = function_to_optimize(xPos,currY)
				if newVal < currValue:
					self.print_flag("CLIMBING BY INC. X "+str(xPos),self.HILL_PROGRESS)
					currValue = newVal
					currX = xPos
					searching = True

			xNeg = currX - step_size

			#Attempt instead to decrease X by the step
			if xNeg >= xmin:
				newVal = function_to_optimize(xNeg,currY)
				if newVal < currValue:
					self.print_flag("CLIMBING BY DEC. X "+str(xNeg),self.HILL_PROGRESS)
					currValue = newVal
					currX = xNeg
					searching = True

			yPos = currY + step_size

			#Attempt to increase Y by the step
			if yPos <= ymax:
				newVal = function_to_optimize(currX,yPos)
				if newVal < currValue:
					self.print_flag("CLIMBING BY INC. Y",self.HILL_PROGRESS)
					currValue = newVal
					currY = yPos
					searching = True

			yNeg = currY - step_size

			#Attempt to decrease Y by the step
			if yNeg >= ymin:
				newVal = function_to_optimize(currX,yNeg)
				if newVal < currValue:
					self.print_flag("CLIMBING BY DEC. Y "+str(yNeg),self.HILL_PROGRESS)
					currValue = newVal
					currY = yNeg
					searching = True

			coord.addX(currX)
			coord.addY(currY)
			coord.addZ(currValue)

		coord.setX(currX)
		coord.setY(currY)
		coord.setValue(currValue)
		self.print_flag("MIN FOUND X:"+str(currX)+" Y:"+str(currY)+" VALUE:"+str(currValue)+"\n",self.HILL)
		return coord

	def hill_climb_random_restart(self, function_to_optimize,step_size,num_restarts,xmin,xmax,ymin,ymax):
		coords = []

		for i in range(0,num_restarts):
			x = random.uniform(xmin,xmax)
			y = random.uniform(ymin,ymax)
			self.print_flag("RESTART "+str(i+1)+"/"+str(num_restarts),self.HILL_RANDOM_PROGRESS)
			self.print_flag("CLIMBING FROM X:"+str(x)+" Y:"+str(y),self.HILL_RANDOM_PROGRESS)
			coords.append(self.hill_climb(function_to_optimize,0.01,-2.5,2.5,-2.5,2.5,x,y))

		mini = coords[0].getValue()
		index = 0
		for i in range(0,len(coords)):
			newVal = coords[i].getValue()
			if newVal < mini:
				mini = newVal
				index = i

		best = coords[index]
		self.print_flag("BEST MIN FOUND X:"+str(best.getX())+" Y:"+str(best.getY())+" VALUE:"+str(best.getValue()),self.HILL_RANDOM)
		return [coords,index]
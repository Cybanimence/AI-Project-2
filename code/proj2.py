from algorithms import Algorithms
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
	
algo = Algorithms()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def main():
#	hill_climb()
	hill_climb_random_restarts()
#	simulated_annealing()
#	plt.show()

def crazyFunction(x,y):
    r = math.sqrt((x**2)+(y**2))
    a1 = math.sin((x**2)+(3*(y**2)))
    a2 = 0.1 + (r**2)
    b = (x**2)+(5*(y**2))
    c = math.exp(1-(r**2))
    return float((a1/a2)+(b*(c/2)))

def hill_climb():
	FUNCTION = crazyFunction
	STEP_SIZE = 0.001
	XMIN = -2.5
	XMAX = 2.5
	YMIN = -2.5
	YMAX = 2.5

	coord = algo.hill_climb(FUNCTION,STEP_SIZE,XMIN,XMAX,YMIN,YMAX)
	print(len(coord.getXPath()))
	x = coord.getXPath()
	y = coord.getYPath()
	z = coord.getZPath()
	ax.plot(x,y,z,label=str("Minimum: \nX:"+
				str(coord.getX())+"\nY:"+
				str(coord.getY())+"\nValue:"+
				str(coord.getValue())))
	ax.set_xlim([-2.5, 2.5])
	ax.set_ylim([-2.5, 2.5])
	ax.legend()

def hill_climb_random_restarts():
	FUNCTION = crazyFunction
	STEP_SIZE = 0.001
	NUM_RESTARTS = 100
	XMIN = -2.5
	XMAX = 2.5
	YMIN = -2.5
	YMAX = 2.5
	coords,index = algo.hill_climb_random_restart(FUNCTION,STEP_SIZE,NUM_RESTARTS,XMIN,XMAX,YMIN,YMAX)
	return
	for i in range(0,len(coords)):
		x = coords[i].getXPath()
		y = coords[i].getYPath()
		z = coords[i].getZPath()
		if i == index:
			ax.plot(x,y,z,label=str("Minimum: \nX:"+
				str(coords[i].getX())+"\nY:"+
				str(coords[i].getY())+"\nValue:"+
				str(coords[i].getValue())))
		else:
			ax.plot(x,y,z)
	ax.set_xlim([-2.5, 2.5])
	ax.set_ylim([-2.5, 2.5])
	ax.legend()

def simulated_annealing():
	FUNCTION = crazyFunction
	STEP_SIZE = 0.001
	TEMPERATURE = 4
	XMIN = -2.5
	XMAX = 2.5
	YMIN = -2.5
	YMAX = 2.5
	coord = algo.simulated_annealing(FUNCTION,STEP_SIZE,TEMPERATURE,XMIN,XMAX,YMIN,YMAX)
	return
	x = coord.getXPath()
	y = coord.getYPath()
	z = coord.getZPath()
	ax.set_xlabel("X axis")
	ax.set_ylabel("Y axis")
	ax.plot(x,y,z,label=str("Minimum: \nX:"+
				str(coord.getX())+"\nY:"+
				str(coord.getY())+"\nValue:"+
				str(coord.getValue())))	
	ax.set_xlim([-2.5, 2.5])
	ax.set_ylim([-2.5, 2.5])
	ax.legend()


main()
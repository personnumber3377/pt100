
from math import sqrt

def f(R_T): # Converts resistance to temperature with the given formula.
	R_0 = 100
	a = 3.9083 * 10**(-3)
	b = -5.775 * 10**(-7)
	k = R_T / R_0
	# Now calculate the answer
	T = (-a+sqrt(a**2-4*b*(1-k)))/(2*b) # Get the positive answer only
	return T

def sol():
	# First human body temperature
	R_T = 110 # ohms
	T = f(R_T)
	print("Solution for human body temp: "+str(T))
	# Then the solution for the environment (room)
	R_T = 108 # ohms
	T = f(R_T)
	print("Solution for the temperature of the room: "+str(T))
	return

if __name__=="__main__":
	sol()
	exit(0)

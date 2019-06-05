
#Calculating area ,perimeter of a crcle and compairing two circles

import math
class Circle:
	def __init__(self,radiusOfCircle):
		self.radiusOfCircle=radiusOfCircle

	def calculateAreaOfCircle(self):
		return 2* math.pi *self.radiusOfCircle**2
	def calculatePerimeterOfCircle(self):
		return 2*math.pi*self.radiusOfCircle
    #Defining less than function
	def __lt__(self,other):
		return self.radiusOfCircle<other.radiusOfCircle
	#Defining less than or equal function	
	def __le__(self,other):
		return self.radiusOfCircle<=other.radiusOfCircle
	#Defining equals function	
	def __eq__(self,other):
		return self.radiusOfCircle==other.radiusOfCircle
	#Defining not equal function
	def __ne__(self,other):
		return self.radiusOfCircle!=other.radiusOfCircle
	#Defining greater than function
	def __gt__(self,other):
		return self.radiusOfCircle>other.radiusOfCircle
	#Defining greater than or equal function
	def __ge__(self,other):
		return self.radiusOfCircle>=other.radiusOfCircle		

firstCircle=Circle(1)
secondCircle=Circle(1)
print("Area of circle is:",int(firstCircle.calculateAreaOfCircle()))
print("Perimeter of circle is:",(firstCircle.calculatePerimeterOfCircle()))

#Comparisions of two objects
print("Both circles equal?:",firstCircle==secondCircle)
print("Checking for less than or equal?:",firstCircle<=secondCircle)
print("Checking for greater than or equal?:",firstCircle>=secondCircle)
print("Checking for greater than?:",firstCircle>secondCircle)
print("Checking for lesser than?:",firstCircle<secondCircle)
print("Checking for not equal?:",firstCircle!=secondCircle)

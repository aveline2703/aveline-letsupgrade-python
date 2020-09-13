
from math import sqrt

class cone():
    def __init__(self,radius,height):
        self.radius = radius
        self.height = height
    def volume(self):
        r = 3.14*self.radius**2*(self.height/3)
        print("Volume of Cone a is : ",r)
    def surfaceArea(self):
        import math
        c = 3.14*self.radius
        d = sqrt(self.radius**2+self.height**2)
        e = (self.radius+d)
        print("Surface Area of a Cone is : " ,c*e)
a = float(input("Enter Radius : "))
b = float(input("Enter Height : "))
x = cone(a,b)
x.volume()
x.surfaceArea()




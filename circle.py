''' Create a Circle class and initialize it with radius.
Make two methods getArea and getCircumference inside this class'''

import math

class circle:
    def __init__(self,radius):
        self.radius=radius

    def getArea(self,):
        return math.pi*self.radius*self.radius

    def getCircumference(self):
        return 2*math.pi*self.radius


rad=circle(float(input('enter the circle radius : ')))

print(' area is : {:.2f}'.format(rad.getArea()))
print('circumference is  : {:.2f}'.format(rad.getCircumference()))
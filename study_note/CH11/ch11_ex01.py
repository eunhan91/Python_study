import math

class circle:
    def __init__(self, radius=0):
        self.__radius=radius
    
    def calc_area(self):
        return (self.__radius**2)*math.pi

    def calc_circum(self):
        return 2*math.pi*self.__radius

    def set_radius(self, radius):
        self.__radius=radius
    
    def get_radius(self):
        return self.__radius
    
r=float(input("원의 반지름: "))
circle1=circle(r)

print("원의 반지름: ", circle1.get_radius())
print("원의 넓이: ", circle1.calc_area())
print("원의 둘레: ", circle1.calc_circum())

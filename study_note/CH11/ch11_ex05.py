class car:
    def __init__(self, color="black", velocity=0, gear=0):
        self.__color=color
        self.__velocity=velocity
        self.__gear=gear

    
    def accelerate(self, value):
        self.__velocity+=value
    
    def decelerate(self, value):
        self.__velocity-=value

    def change_gear(self, value):
        self.__gear=value

    def __str__(self):
        return '(%d, %d, %s)' %(self.__velocity, self.__gear, self.__color)
    
car1=car("white", 100, 3)
print(car1)
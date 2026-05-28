class BOX:
    def __init__(self, width=0, length=0, height=0):
        self.__width=width
        self.__length=length
        self.__height=height

    def set_width(self, width):
        self.__width=width

    def set_length(self, length):
        self.__length=length
    
    def set_height(self, height):
        self.__height=height

    def get_volume(self):
        return self.__width*self.__length*self.__height
    def __str__(self):
        return '(%d, %d, %d)' % (self.__width, self.__length, self.__height)

box=BOX(100, 100, 100)
print(box)

print("상자의 부피는", box.get_volume())
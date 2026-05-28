class Rectangle:
    def __init__(self, height=0, width=0, x=0, y=0): #생성자
        self.__height=height #높이
        self.__width=width #길이
        self.__x=x #x좌표
        self.__y=y #y좌표
    
    def calcArea(self): #사각형의 넓이를 계산하는 calc함수
        return self.__width*self.__height #높이 * 길이
    
    def __str__(self): #str함수를 이용해 나중 출력을 용이하게 하자
        return '(%d,%d), %d, %d' %(self.__x, self.__y, self.__width, self.__height)
    
R1=Rectangle(100, 100, 0, 0) #object 1번 높이와 길이가 100이고 위치가 (0,0)인 객체
R2=Rectangle(200, 200, 10, 10) #object 2번 높이와 길이가 200이고 위치가 (10,10)인 객체

print("box:",R1)
print("box:", R2) #출력
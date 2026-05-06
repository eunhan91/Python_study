def return_many_value(x1,y1,x2,y2):
    
    m=(y2-y1)/(x2-x1) #기울기 식 x1==x2인 경우를 예외처리하는 것이 좋으나 return할 때의 m값이 필요하니 해당 문제에서는 작성하지 않는다.
    y=-x1*m+y1 #직선의 방정식

    return m, y #두개의 value를 return 


x1=float(input("x1 = "))
y1=float(input("y1 = "))
x2=float(input("x2 = "))
y2=float(input("y2 = ")) #직선의 방정식 계산을 위해 두 점의 좌표를 입력받는다. 이때 floating point형태로 자료형을 지정해 기울기 계산(나눗셈)이 용이하게 한다.

m,y=return_many_value(x1,y1,x2,y2) #두개의 값에 대응하는 변수를 만들어서 대입
print("기울기={0:.1f}, y절편={1:.1f}".format(m, y)) #format을 이용하여 간단히 대입
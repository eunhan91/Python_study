import math

pi=math.pi

def area_circle(r):
    return pi*r**2

def circum_circle(r):
    return pi*2*r

r=int(input("원의 반지름을 입력하시오: "))

print("원의 면적:", area_circle(r))
print("원의 둘레:", circum_circle(r))

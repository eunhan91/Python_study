import math

def circle_info(r):
    area = math.pi * r * r
    circumference = 2 * math.pi * r
    return area, circumference

r=float(input("원의 반지름을 입력하시오: "))
result = circle_info(r)
print("원의 넓이는 {}이고 원의 둘레는 {}이다.")
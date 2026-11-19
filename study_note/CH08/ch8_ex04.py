import math

def sphereVolume(r):
    return 4.0/3.0 * math.pi * r**3

r=float(input("구의 반지름을 입력하시오:"))
print(sphereVolume(r))

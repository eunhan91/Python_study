def FtoC(f):
    c=(f-32)*5.0/9.0
    
    return c

fah=float(input("화씨온도를 입력하시오: "))

print(FtoC(fah))
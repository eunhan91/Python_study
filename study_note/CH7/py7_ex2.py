num=int(input("정수를 입력하시오: "))
factorial=1

for x in range(1,num+1):
    factorial*=x

print(num,"!은",factorial,"이다.")
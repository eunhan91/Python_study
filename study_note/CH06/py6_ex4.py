x=int(input("첫 번째 정수: "))
y=int(input("두 번째 정수: "))

if x>y:
    print("큰수는", x)
else:
    if x<y:
        print("큰수는", y)
    else:
        print("두 수가 같다.")
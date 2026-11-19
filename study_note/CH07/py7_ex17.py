from random import randint

num=randint(1,100)

print("1부터 100 사이의 숫자를 맞추시오")

i=1

while i<=10:
    u=int(input("숫자를 입력하시오: "))

    if u == num:
        break
    elif u < num:
        print("높음!")
    else:
        print("낮음!")
    i+=1

if u==num:
    print("축하합니다. 시도횟수=%d" %i)
else:
    print("정답은 %d" %num)

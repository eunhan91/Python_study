from random import randint

num=randint(1,100)

print("숫자 게임에 오신 것을 환영합니다.")

u_num=int(input("숫자를 맞춰 보세요: "))

if num < u_num:
    print("너무 큼!")
elif num > u_num:
    print("너무 작음!")
else:
    print("정답!!")

print("게임 종료")

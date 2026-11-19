from random import randint

c=randint(0,2)

u=input("(가위, 바위, 보) 중에서 하나를 선택하세요: ")

if c == 0:
    c_n="가위"
elif c ==1:
    c_n="바위"
else:
    c_n="보"
print("사용자:", u, "컴퓨터: ",c_n)

if c_n == u:
    print("컴퓨터와 비겼음")
elif (c_n == "가위" and u=="보") or (c_n == "보" and u=="바위") or (c_n =="바위" and u=="가위"):
    print("컴퓨터가 이겼음")

else:
    print("컴퓨터가 졌음")
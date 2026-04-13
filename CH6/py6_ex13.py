mon=int(input("월을 입력하시오"))

if mon==2:
    print("월의 날수는 28일 또는 29일")
elif mon<=7 and mon%2 !=0:
    day=31

else:
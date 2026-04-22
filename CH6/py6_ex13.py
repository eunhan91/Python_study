month=int(input("월을 입력하시오:"))
day=0

if month <= 7:
    if month & 1 == 1:
        day=31
    elif month==2:
        day="28 or 29"
    else:
        day=30        
elif month <=12 and month>=8:
    if month & 1 ==0:
        day=31
    else:
        day=30
else:
    day="undefined"

print("월의 날수는", day)


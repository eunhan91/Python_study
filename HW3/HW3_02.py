def getGrade(score): #점수에 따른 성적 결정함수. elif문을 이용하여 각 분기에 따라 적절한 char을 반환하자
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

score=float(input("점수를 입력하세요: ")) #점수를 입력받는다.
print("성적은 {} 입니다." .format(getGrade(score))) #입력받은 점수에 따라 결정된 함수의 리턴값, 즉 하나의 char을 print문에 끼워넣는다.
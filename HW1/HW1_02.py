#첫점의 좌표 입력받기
#나눗셈 연산으로 실수 형이 될 수 있는 것을 고려해 float형으로 받자
x1=float(input("첫 번째 점의 x좌표:"))
y1=float(input("첫 번째 점의 y좌표:"))

#두번째 점의 좌표 입력받기
x2=float(input("두 번째 점의 x좌표:"))
y2=float(input("두 번째 점의 y좌표:"))

#분모가 0인 상황에 대한 예외처리
if x1 == x2:
    print("x=", x1)
else:
    #기울기 계산
    m=(y2-y1)/(x2-x1)
    #직선의 방정식 계산
    print("직선의 방정식은",m, "x+",-m*x1+y1)



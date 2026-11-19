credit=float(input("이수한 학점수를 입력하시오: "))
GPA=float(input("평점을 입력하시오: "))

if credit>=140 and GPA>=2.0:
    print("졸업하실 수 있습니다.")
else:
    print("졸업이 힘듭니다!")
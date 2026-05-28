H=float(input("근무시간을 입력하시오: "))
MPH=float(input("시간당 임금을 입력하시오: ")) #input함수를 통해 근무시간과 시간당 임금을 입력받기 1.5배 할것을 감안해 float으로 받는다.

#근무시간이 40시간을 넘었는지 확인
if H>40:
    money=40*MPH+(H-40)*MPH*1.5 #40시간 초과시의 임금
else:
    money=H*MPH #40시간 이내 근무시의 임금

print("총임금은", money) #임금값을 출력

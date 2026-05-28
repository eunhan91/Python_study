money = 1000.0 #돈의 초기화
year = 0 #시간의 초기화

while money < 2000: #반복문 탈출 조건: 돈이 두배 이상일 때
    money = money * 1.05 #5%씩 증가
    year += 1 

print("투자 기간:", year)
print("총액:", money)
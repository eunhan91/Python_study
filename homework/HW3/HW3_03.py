def getGCD(a,b):
    if b == 0:
        return a
    
    return getGCD(b, a%b) #재귀함수를 이용하여 유클리드 호재법으로 GCD구하는 함수를 구현

a=int(input("첫 번째 정수: "))
b=int(input("두 번째 정수: ")) #두 정수를 입력받는다.

print(getGCD(a,b)) #결과 출력

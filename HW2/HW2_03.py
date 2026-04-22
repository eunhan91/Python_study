from random import randint   # randint(a, b): a 이상 b 이하의 정수를 무작위로 생성

n = int(input("주사위 실험 횟수를 입력하시오: "))

count = [0] * 13   # 합이 2~12까지 나오므로 인덱스를 편하게 쓰기 위해 13칸 생성

for _ in range(n):   # n번 반복하면서 주사위 2개의 합을 구함
    s = randint(1, 6) + randint(1, 6)   # 주사위 두 개를 던져 나온 합
    count[s] += 1   # 해당 합이 나온 횟수를 1 증가

for i in range(2, 13):   # 가능한 합 2~12에 대해 확률(비율) 출력
    print(i, round(count[i] / n * 100, 3), "%")   # 백분율로 바꿔 소수 셋째 자리까지 출력
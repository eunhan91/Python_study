import math

# 평균을 계산하는 함수
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# 표준 편차를 계산하는 함수
def calculate_std_dev(numbers):
    avg = calculate_average(numbers)
    # 편차의 제곱의 합을 구한 뒤, 데이터의 개수(n)로 나누어 분산을 구함
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    # 분산의 제곱근이 표준 편차
    return math.sqrt(variance)


#정수 리스트 입력받기
user_input = input("정수 리스트 입력: ")

#입력받은 문자열을 공백 기준으로 분리하여 정수 리스트로 변환
num_list = [int(x) for x in user_input.split()]

#작성한 함수들을 호출하여 평균과 표준 편차 계산
average = calculate_average(num_list)
std_dev = calculate_std_dev(num_list)

#결과 출력
print(f"평균= {average}")
print(f"표준 편차 {std_dev}")
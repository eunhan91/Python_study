def reverseList(lst): # 슬라이싱 [::-1]을 사용하여 리스트 전체를 역순으로 복사한 새 리스트를 반환하자
    return lst[::-1]

# 원본 데이터 설정
original = [10, 20, 30, 40, 50]

# 함수 호출하여 역순 리스트 받아오기
result = reverseList(original)

print(result)#print로 리스트를 호출하여 값을 나열하자
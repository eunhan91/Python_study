contacts = {} # 연락처를 저장할 딕셔너리

# 입력 부분
while True:
    name = input("(입력모드)이름을 입력하시오: ")
    if name == "": # 아무것도 안 치고 엔터 누르면 입력 종료
        break
        
    phone = input("전화번호를 입력하시오: ")
    contacts[name] = phone

# 검색 부분
while True:
    name = input("(검색모드)이름을 입력하시오: ") 
    if name == "": # 엔터 치면 전체 종료
        break
        
    # 입력한 이름이 딕셔너리에 존재하는지 확인
    if name in contacts:
        print(name, "의 전화번호는", contacts[name], "입니다.")
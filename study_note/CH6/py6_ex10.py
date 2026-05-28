list=["김철수", "홍길동", "김영희"]
U_passwd=12345678

name=input("아이디를 입력하시오: ")

if name in list:
    passwd=int(input("패스워드를 입력하시오: "))

    if passwd==U_passwd:
        print("환엽합니다.")
    else:
        print("잘못된 패스워드입니다.")
else:
    print("알 수 없는 사용자입니다.")



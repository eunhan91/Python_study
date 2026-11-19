string=input("문자열을 입력하시오:")

alpha=0
digit=0
space=0

for pointer in string:
    if pointer.isalpha():
        alpha+=1
    elif pointer.isdigit():
        digit+=1
    elif pointer.isspace():
        space+=1
print("알파벳 문자의 개수={}\n숫자 문자의 개수={}\n스페이스 문자의 개수={}".format(alpha, digit, space))


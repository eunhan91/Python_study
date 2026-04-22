old=input("계좌 번호를 입력하시오: ")
new=""

for pointer in old:
    if pointer.isdigit():
        new+=pointer
    else:
        continue
print(new)



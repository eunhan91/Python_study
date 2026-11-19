name_list=[]

while True:
    name=input("강아지의 이름을 입력하시오(종료시에는 엔터키) ")

    if name == '':
        break

    name_list.append(name)

for name in name_list:
    print(name, end=", ")


    
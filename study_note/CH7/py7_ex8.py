num=int(input("수를 입력하세요:"))
TF="undefined"

for i in range(2,num):
    if num%i==0:
        TF="False"
        break
    else:
        TF="True"
print("{} is prime ? : {}" .format(num, TF))
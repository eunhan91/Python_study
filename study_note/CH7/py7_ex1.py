max=int(input("어디까지 계산할까요: "))
sum=0

for num in range (max+1):
    sum+=num

print("1부터", num,"까지의 정수의 합=", sum)
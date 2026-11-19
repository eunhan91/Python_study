i=1
total=0

while i<=100:
    if i%3==0:
        total+=i
    i+=1
print("1부터 100사이의 모든 3의 배수의 합은 {}입니다." .format(total))
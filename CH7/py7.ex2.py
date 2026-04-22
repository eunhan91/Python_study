sum=0
i=1

while i <= 100:
    if i%3==0:
        sum+=i
        i+=1
    else:
        i+=1
print("3의 배수의 합은", sum)
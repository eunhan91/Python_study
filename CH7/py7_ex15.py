num=12345
total=0

while num>0:
    total+=num%10
    num//=10
    
    
print("자리수의 합은 %d입니다." %total)
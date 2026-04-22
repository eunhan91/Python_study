num=int(input("계산할 팩토리얼을 입력하세요"))
facto=num

while num>0:
    facto*=num
    num-=1

print(facto,"가 팩토리얼값")
    

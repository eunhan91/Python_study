count=0

string=input("문자열을 입력하시오: ")

count=len(string)

if count%2==1:
    ch1=string[count//2]
    print("중앙글자는 ", ch1)
else:
    ch1=string[count//2-1]
    ch2=string[count//2]
    print("중앙글자는 ", ch1, ch2)



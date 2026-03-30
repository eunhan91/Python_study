price=int(input("물건값을 입력하시오:"))
th=int(input("1000원 지폐 개수"))
FH=int(input("500원 동전 개수"))
OH=int(input("100원 동전 개수"))

change=-price+1000*th+500*FH+100*OH

print("500원=", change//500,"100원=", change%500//100, "10원=", change%100//10, "1원=", change%10)
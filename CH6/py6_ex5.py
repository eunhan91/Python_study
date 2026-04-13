price=float(input("구입 금액을 입력하시오: "))

if price >= 100000:
    price-=price*0.05

print("지불 금액은",price, "입니다.")
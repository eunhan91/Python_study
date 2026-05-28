def is_prime(num):
    prime=True

    for i in range(2, num):
        if num%i==0:
            prime=False
    
    return prime


number=int(input("정수를 입력하시오:"))
print(is_prime(number))
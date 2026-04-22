prime=[]

for x in range(2,101):
    is_prime=True

    for i in range(2,x):
        if x%i == 0:
            is_prime=False
    
    if is_prime:
        prime.append(x)

print(prime)

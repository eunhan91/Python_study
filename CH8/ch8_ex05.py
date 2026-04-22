import random

def genpass():
    
    password=""

    for i in range(6):

        setting=random.randint(0,1)

        if setting==0:
            digit=random.randint(0,9)
            password+=str(digit)
        else:
            alpha=random.randint(97,122)
            password+=chr(alpha)
    return password

print(genpass())

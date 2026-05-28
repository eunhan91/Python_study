class account:
    def __init__(self):
        self.balance=0
    
    def withdraw(self, money=0):
        self.balance-=money
    
    def deposit(self, money=0):
        self.balance+=money
            
ac=account()
money=100

ac.deposit(money)
print("통장에", money, "원이 입금되었습니다.")

money=10

ac.withdraw(money)
print("통장에", money, "원이 출금되었씁니다.")

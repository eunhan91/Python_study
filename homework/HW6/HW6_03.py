class BankAccount(object):
    interest_rate=0.3 #매소드의 밖에서 선언된 클래스 변수 클래스에 따라 생성된 모든 객체들이 공유하는 값이다.

    def __init__(self, name, number, balance):
        self.__name=name #매소드 내에서 선언된 인스턴스 변수
        self.__number=number #매소드 내에서 선언된 인스턴스 변수
        self.__balance=balance #매소드 내에서 선언된 인스턴스 변수
        return
    
    def deposit(self, amount):
        self.__balance+=amount #amout를 입력받고 입력 받은 만큼의 amout를 잔액에서 증가시킨다,

    def withdraw(self, amount):
        self.__balance-=amount #amout를 입력받고 입력 받은 만큼의 amout를 잔액에서 감소시킨다,
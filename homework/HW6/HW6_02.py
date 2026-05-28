class Employee:
    empCount=0 #클래스 변수 선언

    def __init__(self, name, salary): #생성자
        self.__name=name
        self.__salary=salary
        Employee.empCount+=1 #object가 생길때 마다 empCount값에 +1

    def displayCount(self):
        print(Employee.empCount) #empCount값을 출력하는 함수

    def displayEmployee(self):
        print(self.__name)
        print(self.__salary) #self의 이름과 월급 값을 출력
    
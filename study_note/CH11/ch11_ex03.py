class cat:
    def __init__(self, name=None, age=0):
        self.__name=name
        self.__age=age

    def set_cat(self, name, age):
        self.__name=name
        self.__age=age

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
M=cat("Missy", 3)
L=cat("Lucky", 5)

print(M.get_name(), M.get_age())
print(L.get_name(), L.get_age())



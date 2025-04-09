class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance 
    
obj = BankAccount('Gary', 20000)
print(obj.get_balance())

# class Protected:
#     def __init__(self):
#         self._salary = 40000
        
#     def salary(self):
#         return self._salary
    
# obj = Protected()
# print(obj.salary)
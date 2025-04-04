# class Private:
#     def __init__(self):
#         self.__salary = 50000
    
#     def salary(self):
#         return self.__salary 
    
# obj = Private()
# print(obj.salary())

# class Protected:
#     def __init__(self):
#         self._salary = 40000
        
#     def salary(self):
#         return self._salary
    
# obj = Protected()
# print(obj.salary)

# class Private:
#     def __init__(self):
#         self.__salary = 50000
    
#     def salary(self):
#         return self.__salary 
    
# obj = Private()
# print(obj.salary())

class Public:
    def __init__(self):
        self.salary = 40000
        
    def salary(self):
        return self.salary
    
obj = Public()
print(obj.salary)
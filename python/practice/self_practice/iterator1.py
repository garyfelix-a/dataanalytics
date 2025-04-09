class EvenNum:
    def __init__(self):
        self.num = 1
        
    def __iter__(self):
        return self

    def __next__(self):
        while self.num <= 10:
            if self.num % 2 == 0:
                even = self.num 
                self.num += 1
                return even
            self.num += 1
        raise StopIteration
    
even_iter = EvenNum()

for num in even_iter:
    print(num, end=" ")
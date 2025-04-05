import array

fruits = array.array('u', "applecherry")
print(fruits[0])

for fruit in fruits:
    print(fruit)
    
print("\n")
    
numbers = array.array('i', [5,2,3,4,1])
length = len(numbers)
print(length)

print("\n")

sorted_numbers = sorted(numbers)
print(sorted_numbers)
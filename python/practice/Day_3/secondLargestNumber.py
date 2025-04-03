numbers = {2, 2, 1, 5, 32, 21}

def second_large_num(num_set):
    max = float('-inf')
    second_max = float('-inf')
    
    for i in num_set:
        if i > max:
            max = i
            
    for i in num_set:
        if i > second_max and i < max:
            second_max = i
            
    return second_max if second_max != float('-inf') else "No second largest value"
    

print(second_large_num(numbers))
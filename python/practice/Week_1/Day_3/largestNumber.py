list = [33, 2, 21, 90, -1, 22, 1, 100]

def find_large_num(list):
    max = 0
    for i in list:
        if i > max:
            max = i
    return max

print(find_large_num(list))
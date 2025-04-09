list1 = [2, 1, 3, 5, 4]

# selection sorting
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        idx = i 
        for j in range(i+1, n):
            if arr[j] < arr[idx]:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
        
    return arr
        
print(selection_sort(list1))
    
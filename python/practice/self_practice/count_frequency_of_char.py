text = "hello"

# empty dictionary to store count
freq = {}

# loops through each character in the string
for i in text:
    # checks if character is already in dictionary or not
    # if yes, get current count and add +1
    # if no, it returns 0
    freq[i] = freq.get(i, 0) + 1 
    
print("Character frequencies:")
for i, count in freq.items():
    print(f"{i}: {count}")
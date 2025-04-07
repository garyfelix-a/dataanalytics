str = input("Enter a string to calculate vowel count: ")

def count_vowel(text):
    count = 0
    vowels = 'aeiou'
    for i in text:
        for j in vowels:
            if i in j:
                count = count + 1
    
    return count

print(count_vowel(str))
    
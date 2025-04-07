mark = int(input("Enter your mark: "))

if mark >= 90 and mark <= 100:
    print("You got O Grade")
elif mark >=80 and mark < 90:
    print("You got A+ Grade")
elif mark >=70 and mark <80:
    print("You got A Grade")
elif mark >=60 and mark <70:
    print("You got B Grade")
else:
    print("You got F Grade")
    
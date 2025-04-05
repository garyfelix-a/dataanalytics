import re

# x = "The rain is spain"
# y = re.search("^The.*spain$", x)

# if y:
#     print("Yes matched")
# else:
#     print("Not matched")
    
# a = "The rain is spain"
# z = re.findall("ai", a)
# print(z)

# Z = re.search("\s", a)
# print(Z)

# pattern = r"\d+"
# text = "There are 123 apples"
# match = re.search(pattern, text)
# if match:
#     print("Match found", match.group())

# pattern = r"Hello"
# text = "Hello, world!"
# match = re.match(pattern, text)

# pattern = r"(\d+)-(\d+)-(\d+)"
# text = "The event id on 2025-03-26"
# match = re.search(pattern, text)
# if match:
#     print("Year: ", match.group(1))
#     print("Month: ", match.group(2))
#     print("Day: ", match.group(3))

# Email Pattern Checking

email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
text = "Please contact us at: example@example.com" 
match = re.search(email_pattern, text)

if match:
    print("Email found: ", match.group())
else:
    print("Email not found")
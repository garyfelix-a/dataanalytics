import re

# text = "Hello, Email: abc@abc.com"
# match = re.search(r"^[\w.-]+@[\w.-]+\.\[\w+]", text)

# print(match)


pattern = "^.*(?=.*{8,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$%&+=]).*$"

text = input()

match = re.match(pattern, text)
if match:
    print("valid")
else:
    print("invalid")
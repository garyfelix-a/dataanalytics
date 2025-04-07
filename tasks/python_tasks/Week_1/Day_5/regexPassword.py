import re

pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
# pattern = r'[A-Za-z0-9@#$%^&+=]{8,}'
password = input("Enter your password: ")

match = re.match(pattern,password)
if match:
    print("Valid password")
else:
    print("Invalid password")
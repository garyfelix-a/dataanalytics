import re

pattern = "^https?://[^\s/$.?#].[^\d]*$"
url = input("Enter a URL: ")
match = re.findall(pattern, url)

if match:
    print("URL is valid")
else:
    print("URL is invalid")
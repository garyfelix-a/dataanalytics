import json

x = '{"name": "xyx", "age": 35}'   #json format
z = json.loads(x)

print(z["name"])
print(z["age"])

# dictionary to json
X = {
    "name":"xyx",
    "age": 33
}

Y = json.dumps(X)
print(Y)

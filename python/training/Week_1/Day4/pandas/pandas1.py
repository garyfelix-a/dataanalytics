import pandas as pd

data = {
    'name': ['Rock', 'Adam'],
    'age': [22, 23],
    'city': ['Texas', 'Florida']
}
# print(df[df['Age']>21])
df = pd.DataFrame(data)
print(df)

print(df[df['age'] < 23])
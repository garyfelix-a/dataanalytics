import pandas as pd

# s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

# print(s)

data = {
    'Name': ['Alice', 'Bob', 'George'],
    'Age' : [21, 22, 23],
    'City' : ['Salem', 'Chennai', 'Coimbatore']
}

df = pd.DataFrame(data)
print(df)
print(df.head())
print("info:", df.info())
print("describe: ",df.describe())
print(df.columns)
print(df.shape)

# selection and filtering
print(df['Age'])
print(df[['Name', 'City']])
print(df[df['Age']>21])
print(df['Age'])
print(df['Age'])

df['Age']+=1

print(df)
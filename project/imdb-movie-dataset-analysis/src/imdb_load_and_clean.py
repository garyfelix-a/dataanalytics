import pandas as pd
import os

print("Current working directory", os.getcwd())

data = pd.read_csv("data/raw/imdb_top_1000.csv")

print(data.head())
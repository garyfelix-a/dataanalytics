import pandas as pd
import numpy as np
import os

def clean_suicide_data(input_path, output_path):
    df = pd.read_csv(input_path)
    print("Original data shape", df.shape)
    
    # drop duplicates
    df.drop_duplicates(inplace=True)
    
    # rename columns for consistency
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # Handling missing values & count of null values
    print("\nMissing values before cleaning:")
    print(df.isnull().sum())
    
    df['suicides_no'] = df['suicides_no'].fillna(0).astype(int)
    df['population'] = df['population'].fillna(0).astype(int)
    df['country-year'] = df['country-year'].fillna(method='ffill') # forward fill
    df['gdp_for_year'] = df['gdp_for_year'].str.replace(',', '').astype(float)
    
    # Fill the rest with 0 or keep them for manual inspection
    df.fillna(0, inplace=True)
    
    print("\nMissing values after cleaning:")
    print(df.isnull().sum())
    
    # save clean data
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\nCleaned data saved to: {output_path}")
    
if __name__ == "__main__":
    raw_path = "data/raw/master.csv"
    cleaned_path = "data/clean/suicide_data_cleaned.csv"
    clean_suicide_data(raw_path, cleaned_path)
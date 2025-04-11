import pandas as pd
import os

# cleans raw data (like missing value, formatting issues, duplicates, etc)
# cleaned data is saved seperately in a new folder.  
def clean_imdb_data(input_path, output_path):
    # load the dataset
    df = pd.read_csv(input_path)
    # shape of the table (1000, 16)
    print("Original Data Shape:", df.shape)
    
    # Drop duplicates
    df.drop_duplicates(inplace=True)
    
    # Standardize Column names
    # removes leading spaces, converts to lowercase, replace space with underscore
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # check for missing values
    print("\nMissing values before cleaning:")
    print(df.isnull().sum())
    
    # clean released_year (convert to numeric, coerce errors)
    # setting errors = 'coerce' will convert non-numeric values to NaN without raising an error.
    df['released_year'] = pd.to_numeric(df['released_year'], errors='coerce')
    # if missing file, it is filled with most common year
    df['released_year'] = df['released_year'].fillna(df['released_year'].mode()[0])
    
    # Fills missing certificate with 'Not Rated'
    df['certificate'] = df['certificate'].fillna('Not Rated')
    
    # Clean runtime: remove "min", convert to int
    # eg., '120 min' -> '120', min word is removed
    df['runtime'] = df['runtime'].str.replace('min', '').astype(int)
    
    # Clean gross: remove commas, convert to numeric
    # eg., '1,000,000' -> '1000000' (commas is removed)
    df['gross'] = df['gross'].str.replace(',', '')
    df['gross'] = pd.to_numeric(df['gross'], errors='coerce')
    
    # missing values is filled with the median gross values
    df['gross'] = df['gross'].fillna(df['gross'].median())
    
    # Fill missing meta score with median
    df['meta_score'] = df['meta_score'].fillna(df['meta_score'].median())
  
    # Show missing after cleaning
    print("\nMissing values after cleaning:")
    print(df.isnull().sum())

    # Save cleaned data
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\nCleaned data saved to: {output_path}")
    
if __name__ == "__main__":
    raw_path = "C:/Users/Sharley Angel/OneDrive/Desktop/Git-training/dataanalytics/project/imdb-movie-dataset-analysis/data/raw/imdb_top_1000.csv"
    cleaned_path = "C:/Users/Sharley Angel/OneDrive/Desktop/Git-training/dataanalytics/project/imdb-movie-dataset-analysis/data/clean/imdb_top_1000.csv"
    clean_imdb_data(raw_path, cleaned_path)

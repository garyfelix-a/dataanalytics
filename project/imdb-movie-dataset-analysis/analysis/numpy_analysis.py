import numpy as np
import pandas as pd
import os
from imdb_analysis import load_data

# this function creates a new col in data frame based on IMDB ratings
def add_rating_category(df):
    ratings = df['imdb_rating'].to_numpy()
    categories= np.where(ratings >= 8.5, 'Excellent',
                np.where(ratings>=7.5, 'Good',
                np.where(ratings >= 6.5, 'Average', 'Poor')))
    df['rating_category'] = categories
    return df

# this function analyzes IMDB ratings over the years
def year_wise_trends(df):
    years = df['released_year'].unique()
    years.sort()
    stats = []
    for year in years:
        data = df[df['released_year'] == year]
        ratings = data['imdb_rating'].to_numpy()
        stats.append((year, np.mean(ratings), np.median(ratings), np.std(ratings)))
    
    return stats


if __name__ == "__main__":
    df = load_data()
    print(df.head())
    
    print("\nRatings Category:")
    print(add_rating_category(df))
    
    print("\nYear wise trends:")
    print(year_wise_trends(df))
    
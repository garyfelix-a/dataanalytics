import pandas as pd
import numpy as np
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

# load clean data from SQL Database
def load_data():
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")
    
    # connect to MySQL
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    
    query = "SELECT * FROM top_1000_movies"
    df = pd.read_sql(query, conn)
    conn.close()
    
    return df

# Returns top n directors who directed the most movies.
def top_directors(df, n=10):
    # value_counts() --> counts how many times each director appears & head(n) --> returns top (n) data.
    return df['director'].value_counts().head(n)

# Returns the top n most common genres, if genres are listed together, then it is seperated using split() and stored into single list(stack())
def top_genres(df, n=10):
    all_genres = df['genre'].str.split(', ', expand=True).stack()
    return all_genres.value_counts().head(n)

# Shows the statistical summary of IMDB ratings
# it returns count, mean, std, min, 25%, 50%, 75%, max
def rating_distribution(df):
    return df['imdb_rating'].describe()

# Calculates correlation between number of votes and IMDB rating
# Correlation means calculating how votes and ratings are linearly related
def votes_vs_rating_correlation(df):
    # converting both columns to numpy arrays
    votes = df['no_of_votes'].to_numpy()
    ratings = df['imdb_rating'].to_numpy()
    # accesses the correlation value between votes and ratings
    # value close to 1 -> strong positive relation  
    # value close to -1 -> strong negative
    # value close to 0 -> no correlation
    return np.corrcoef(votes, ratings)[0, 1]

# Find actors who have a high variation in ratings among their movies
def actor_rating_std(df):
    # for each column it is calculated
    actors = ['star1', 'star2', 'star3', 'star4']
    actor_ratings = {}
    # based on actors, calculating the mean, standard deviation(higher = more variation), total count actor acted.
    for actor in actors:
        grouped = df.groupby(actor)['imdb_rating'].agg(['mean', 'std', 'count'])
        filtered = grouped[grouped['count'] >= 3]
        actor_ratings[actor] = filtered.sort_values(by='std', ascending=False)
        
    return actor_ratings
    

if __name__ == "__main__":
    df = load_data()
    print("Loaded Data Shape", df.shape)
    print(df.head())
    
    print("\n Top Directors")
    print(top_directors(df))
    
    print("\n Top Genres")
    print(top_genres(df))
    
    print("\n Ratings Description")
    print(rating_distribution(df))
    
    print("\nCorrelation between Votes and Ratings:")
    print(votes_vs_rating_correlation(df))
    
    print("\nStandard Deviation of Ratings (by actors):")
    actor_stds = actor_rating_std(df)
    for actor, data in actor_stds.items():
        print(f"\nActor Group: {actor}")
        print(data.head(3))
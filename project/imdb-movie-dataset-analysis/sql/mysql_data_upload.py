import mysql.connector
import pandas as pd
import os

from dotenv import load_dotenv

load_dotenv()

def connect_to_db():
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
    
    return conn
    
def insert_into_mysql(csv_path):
    # load cleaned data
    df = pd.read_csv(csv_path)
    # database connection
    conn = connect_to_db()
    cursor = conn.cursor()
    
    # insert query
    insert_query = """
    INSERT INTO top_1000_movies 
    (series_title, released_year, certificate, runtime, genre, imdb_rating, overview, meta_score, director, star1, star2, star3, star4, no_of_votes, gross)
    VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    for _, row in df.iterrows():
        values = (
            row['series_title'],
            int(row['released_year']),
            row['certificate'],
            int(row['runtime']),
            row['genre'],
            float(row['imdb_rating']),
            row['overview'],
            float(row['meta_score']),
            row['director'],
            row['star1'],
            row['star2'],
            row['star3'],
            row['star4'],
            int(row['no_of_votes']),
            int(row['gross'])
        )
        
        cursor.execute(insert_query, values)
        
    conn.commit()
    print("Data inserted successfully into imdb_analysis")
    cursor.close()
    conn.close()
    

if __name__ == "__main__":
    csv_path = "C:/Users/Sharley Angel/OneDrive/Desktop/Git-training/dataanalytics/project/imdb-movie-dataset-analysis/data/clean/imdb_top_1000.csv"
    insert_into_mysql(csv_path)    
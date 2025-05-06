import pandas as pd
import plotly.express as px
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import re

load_dotenv()

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

db_url = f"mysql+pymysql://{user}:{password}@{host}/{database}"
engine = create_engine(db_url)

# Output directory
output_dir = "C:/Users/Sharley Angel/OneDrive/Desktop/Git-training/dataanalytics/project/imdb-movie-dataset-analysis/outputs/plots"
os.makedirs(output_dir, exist_ok=True)

# Function to clean filenames
def sanitize_filename(name):
    return re.sub(r'[<>:"/\\|?*]', '_', name)

# Save plots as both HTML and PNG
def save_plot(fig, name):
    safe_name = sanitize_filename(name)
    html_path = os.path.join(output_dir, f"{safe_name}.html")
    png_path = os.path.join(output_dir, f"{safe_name}.png")
    
    try:
        fig.write_html(html_path)
        print(f"Saved HTML: {html_path}")
    except Exception as e:
        print(f"Error saving HTML: {e}")

    try:
        fig.write_image(png_path)
        print(f"Saved PNG: {png_path}")
    except Exception as e:
        print(f"Error saving PNG (check if kaleido is installed): {e}")

# Chart 1
def top_directors():
    query = """
        SELECT director, COUNT(*) AS movie_count
        FROM top_1000_movies
        GROUP BY director
        ORDER BY movie_count DESC
        LIMIT 10
    """
    df = pd.read_sql(query, engine)
    fig = px.bar(df, x='director', y='movie_count', title='Top 10 Directors with Most Movies')
    fig.show(renderer="browser")
    save_plot(fig, "top_10_directors")

# Chart 2
def genre_ratings():
    query = "SELECT genre, imdb_rating FROM top_1000_movies"
    df = pd.read_sql(query, engine)
    df['genre'] = df['genre'].str.split(',')
    df = df.explode('genre')
    df['genre'] = df['genre'].str.strip()
    genre_avg_rating = df.groupby('genre')['imdb_rating'].mean().sort_values(ascending=False).reset_index()
    fig = px.bar(genre_avg_rating, x='genre', y='imdb_rating', title='Average IMDb Rating by Genre')
    fig.show(renderer="browser")
    save_plot(fig, "average_imdb_rating_by_genres")

# Chart 3
def yearly_trends():
    query = """
        SELECT released_year, AVG(imdb_rating) AS imdb_rating
        FROM top_1000_movies
        GROUP BY released_year
        ORDER BY released_year
    """
    df = pd.read_sql(query, engine)
    fig = px.line(df, x='released_year', y='imdb_rating', title='Yearly Average IMDb Rating')
    fig.show(renderer="browser")
    save_plot(fig, "yearly_average_imdb_rating")

# Chart 4
def gross_vs_rating():
    query = """
        SELECT imdb_rating, gross, no_of_votes, series_title, released_year
        FROM top_1000_movies
        WHERE gross IS NOT NULL AND gross != 0
    """
    df = pd.read_sql(query, engine)
    fig = px.scatter(df, x='imdb_rating', y='gross', size='no_of_votes', color='released_year',
                     hover_data=['series_title'], title='Gross vs IMDb Rating')
    fig.update_traces(marker=dict(size=6))  # Prevent browser lag
    fig.show(renderer="browser")
    save_plot(fig, "gross_vs_imdb_rating")

# Chart 5
def underrated_movies():
    df = pd.read_sql("SELECT series_title, imdb_rating, no_of_votes FROM top_1000_movies", engine)
    q1 = df['no_of_votes'].quantile(0.25)
    df = df[df['no_of_votes'] < q1].sort_values(by='imdb_rating', ascending=False).head(10)
    fig = px.bar(df, x='series_title', y='imdb_rating',
                 title='Top 10 Underrated Movies (Low Votes, High Rating)',
                 hover_data=['no_of_votes'])
    fig.show(renderer="browser")
    save_plot(fig, "top_underrated_movies")

# Chart 6
def top_genres():
    df = pd.read_sql("SELECT genre FROM top_1000_movies", engine)
    all_genres = df['genre'].str.split(', ', expand=True).stack()
    top_genres = all_genres.value_counts().nlargest(10).reset_index()
    top_genres.columns = ['genre', 'movie_count']
    fig = px.bar(top_genres, x='genre', y='movie_count', title='Top 10 Genres with Most Movies')
    fig.show(renderer="browser")
    save_plot(fig, "top_10_genres")

# Chart 7
def decade_votes():
    query = """
        SELECT (released_year DIV 10) * 10 AS decade, SUM(no_of_votes) AS no_of_votes
        FROM top_1000_movies
        GROUP BY decade
        ORDER BY decade
    """
    df = pd.read_sql(query, engine)
    fig = px.bar(df, x='decade', y='no_of_votes', text='no_of_votes',
                 title='Decade-wise Total Number of Votes')
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(xaxis_title="Decade", yaxis_title="Total Votes")
    fig.show(renderer="browser")
    save_plot(fig, "decade_votes")

# Chart 8
def best_per_decade():
    query = """
        WITH decade_ranks AS (
            SELECT *, 
                (released_year DIV 10) * 10 AS decade,
                ROW_NUMBER() OVER (PARTITION BY (released_year DIV 10) * 10 ORDER BY imdb_rating DESC) AS rnk
            FROM top_1000_movies
        )
        SELECT decade, series_title, imdb_rating
        FROM decade_ranks
        WHERE rnk = 1
        ORDER BY decade;
    """
    df = pd.read_sql(query, engine)
    fig = px.treemap(
        df,
        path=['decade', 'series_title'],
        values='imdb_rating',
        color='imdb_rating',
        title='Best Movie of Each Decade (Treemap)',
        color_continuous_scale='viridis'
    )
    fig.show(renderer="browser")
    save_plot(fig, "Best_Movie_of_Each_Decade_(Treemap)")

# CLI Menu
def main():
    while True:
        print("\n====== IMDb Movie Dataset Analysis ======")
        print("1. Top 10 Directors with Most Movies")
        print("2. Average IMDb Rating by Genre")
        print("3. Yearly Average IMDb Rating Trend")
        print("4. Gross vs IMDb Rating (Scatter Plot)")
        print("5. Top 10 Underrated Movies")
        print("6. Top 10 Genres with Most Movies")
        print("7. Decade-wise Total number of Votes")
        print("8. Best Movie of Each Decade (Treemap)")
        print("0. Exit")

        choice = input("Enter your choice (0-8): ")

        if choice == '1':
            top_directors()
        elif choice == '2':
            genre_ratings()
        elif choice == '3':
            yearly_trends()
        elif choice == '4':
            gross_vs_rating()
        elif choice == '5':
            underrated_movies()
        elif choice == '6':
            top_genres()
        elif choice == '7':
            decade_votes()
        elif choice == '8':
            best_per_decade()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

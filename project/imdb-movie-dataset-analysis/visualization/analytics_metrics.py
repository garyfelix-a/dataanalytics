import pandas as pd
import plotly.express as px
import os

# Load data
csv_path = "C:/Users/Sharley Angel/OneDrive/Desktop/Git-training/dataanalytics/project/imdb-movie-dataset-analysis/data/clean/imdb_top_1000.csv"
df = pd.read_csv(csv_path)

# 1. Top Underrated Movies (Low votes, High rating)
underrated = df[df['no_of_votes'] < df['no_of_votes'].quantile(0.25)]
underrated = underrated.sort_values(by='imdb_rating', ascending=False).head(10)

fig1 = px.bar(underrated, x='series_title', y='imdb_rating',
              title='Top 10 Underrated Movies (Low Votes, High Rating)',
              hover_data=['no_of_votes'])
fig1.write_html("output/plots/top_underrated_movies.html")
fig1.write_image("output/plots/top_underrated_movies.png")

# 2. Director Impact Score = Avg Rating × Number of Movies
director_stats = df.groupby('director').agg(
    avg_rating=('imdb_rating', 'mean'),
    movie_count=('series_title', 'count')
)
director_stats['impact_score'] = director_stats['avg_rating'] * director_stats['movie_count']
top_directors = director_stats.sort_values(by='impact_score', ascending=False).head(10).reset_index()

fig2 = px.bar(top_directors, x='director', y='impact_score',
              title='Top 10 Directors by Impact Score',
              hover_data=['avg_rating', 'movie_count'])
fig2.write_html("output/plots/director_impact_score.html")
fig2.write_image("output/plots/director_impact_score.png")

# 3. Star Power Index = Avg Rating per Actor (considering Star1 only for now)
star_power = df.groupby('star1')['imdb_rating'].mean().sort_values(ascending=False).head(10).reset_index()
star_power.columns = ['actor', 'star_power_index']

fig3 = px.bar(star_power, x='actor', y='star_power_index',
              title='Top 10 Actors by Star Power Index (Avg Rating)',
              hover_data=['star_power_index'])
fig3.write_html("output/plots/star_power_index.html")
fig3.write_image("output/plots/star_power_index.png")

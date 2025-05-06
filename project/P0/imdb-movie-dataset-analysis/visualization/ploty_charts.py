import pandas as pd
import numpy as np
import plotly.express as px
import os

csv_path = "C:/Users/Sharley Angel/OneDrive/Desktop/Git-training/dataanalytics/project/imdb-movie-dataset-analysis/data/clean/imdb_top_1000.csv"
df = pd.read_csv(csv_path)
print(df.head())

output_dir = "C:/Users/Sharley Angel/OneDrive/Desktop/Git-training/dataanalytics/project/imdb-movie-dataset-analysis/outputs/plots"
os.makedirs(output_dir, exist_ok=True)

def save_plot(fig, name):
    html_path = os.path.join(output_dir, f"{name}.html")
    png_path = os.path.join(output_dir, f"{name}.png")
    fig.write_html(html_path)
    fig.write_image(png_path)
    print(f"Saved {name} as HTML and PNG")

# Chart 1: Top 10 Directors with Most Movies
director_counts = df['director'].value_counts().nlargest(10).reset_index()
director_counts.columns = ['director', 'movie_count']
fig1 = px.bar(director_counts, x='director', y='movie_count', title='Top 10 Directors with Most Movies With High Ratings')
fig1.show()
save_plot(fig1, "top_10_directors")

# Chart 2: Top Genres by Average IMDb Rating
# First, expand multiple genres
genre_rating = df[['genre', 'imdb_rating']].copy()
genre_rating['genre'] = genre_rating['genre'].str.split(',')
genre_exploded = genre_rating.explode('genre')
genre_exploded['genre'] = genre_exploded['genre'].str.strip()

genre_avg_rating = genre_exploded.groupby('genre')['imdb_rating'].mean().sort_values(ascending=False).reset_index()
fig2 = px.bar(genre_avg_rating, x='genre', y='imdb_rating', title='Average IMDb Rating by Genre')
fig2.show()
save_plot(fig2, "average_imdb_rating_by_genres")

# Chart 3: Yearly Trend of Average Ratings
yearly_avg_rating = df.groupby('released_year')['imdb_rating'].mean().reset_index()
yearly_avg_rating = yearly_avg_rating.sort_values('released_year')
fig3 = px.line(yearly_avg_rating, x='released_year', y='imdb_rating', title='Yearly Average IMDb Rating')
fig3.show()
save_plot(fig3, "yearly_average_imdb_rating")

# Chart 4: Gross vs IMDb Rating (Bubble Plot)
df_gross = df[df['gross'] != 0]  # Remove missing gross
df_gross['gross'] = pd.to_numeric(df_gross['gross'], errors='coerce')
fig4 = px.scatter(df_gross, x='imdb_rating', y='gross', size='no_of_votes', color='released_year',
                  hover_data=['series_title'], title='Gross vs IMDb Rating')
fig4.show()
save_plot(fig4, "gross_vs_imdb_rating")

# # Chart 5: Votes Distribution (Histogram)
# fig5 = px.histogram(df, x='no_of_votes', nbins=50, title='Distribution of Number of Votes')
# fig5.show()
# save_plot(fig5, "distribution_of_number_of_votes")

# Chart 6: Top Underrated Movies (Low votes, high rating)
underrated = df[df['no_of_votes'] < df['no_of_votes'].quantile(0.25)]
underrated = underrated.sort_values(by='imdb_rating', ascending=False).head(10)
fig6 = px.bar(underrated, x='series_title', y='imdb_rating',
              title='Top 10 Underrated Movies (Low Votes, High Rating)',
              hover_data=['no_of_votes'])
fig6.show()
save_plot(fig6, "top_underrated_movies")

# Chart 7: Director Impact Score = Avg Rating × Number of Movies
# director_stats = df.groupby('director').agg(
#     avg_rating=('imdb_rating', 'mean'),
#     movie_count=('series_title', 'count')
# )
# director_stats['impact_score'] = director_stats['avg_rating'] * director_stats['movie_count']
# top_directors = director_stats.sort_values(by='impact_score', ascending=False).head(10).reset_index()

# fig7 = px.bar(top_directors, x='director', y='impact_score',
#               title='Top 10 Directors by Impact Score',
#               hover_data=['avg_rating', 'movie_count'])
# fig7.show()
# save_plot(fig7, "director_impact_score")

# Chart 8: Star Power Index = Avg IMDb Rating for each Actor (using star1)
star_power = df.groupby('star1')['imdb_rating'].mean().sort_values(ascending=False).head(10).reset_index()
star_power.columns = ['actor', 'star_power_index']

fig8 = px.bar(star_power, x='actor', y='star_power_index',
              title='Top 10 Actors by Star Power Index (Average IMDb Rating)',
              hover_data=['star_power_index'])
fig8.show()
save_plot(fig8, "star_power_index")

# Chart 9: Top 10 Genres with Most movies
all_genres = df['genre'].str.split(', ', expand=True).stack()
top_genres = all_genres.value_counts().nlargest(10).reset_index()
top_genres.columns = ['genre', 'movie_count']
fig9 = px.bar(top_genres, x='genre', y='movie_count', title='Top 10 Genres with Most Movies')
fig9.show()
save_plot(fig9, "top_10_genres")

# Chart 10: Decade wise total number of votes
df['decade'] = (df['released_year'] // 10) * 10
decade_votes = df.groupby('decade')['no_of_votes'].sum().reset_index()
fig10 = px.bar(decade_votes, x='decade', y='no_of_votes', text='no_of_votes',
              title='Decade-wise Total Number of Votes')
fig10.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig10.update_layout(xaxis_title="Decade", yaxis_title="Total Votes")
fig10.show()
save_plot(fig10, "decade_votes")

# Chart 11: Decade wise best film
df['decade'] = (df['released_year']//10) * 10
best_per_decade = df.loc[df.groupby('decade')['imdb_rating'].idxmax()][['decade', 'series_title', 'imdb_rating']]
best_per_decade = best_per_decade.sort_values('decade')
fig11 = px.treemap(
    best_per_decade,
    path=['decade', 'series_title'],
    values='imdb_rating',
    color='imdb_rating',
    title='Best Movie of Each Decade (Treemap)',
    color_continuous_scale='Blues'
)
fig11.show()
save_plot(fig11, "decade-wise best film")
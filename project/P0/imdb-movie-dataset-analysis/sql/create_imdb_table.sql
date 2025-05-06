use imdb_analysis;

CREATE TABLE top_1000_movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    series_title VARCHAR(255),
    released_year INT,
    certificate VARCHAR(50),
    runtime INT,
    genre VARCHAR(255),
    imdb_rating FLOAT,
    overview TEXT,
    meta_score FLOAT,
    director VARCHAR(255),
    star1 VARCHAR(255),
    star2 VARCHAR(255),
    star3 VARCHAR(255),
    star4 VARCHAR(255),
    no_of_votes INT,
    gross BIGINT
);

select * from top_1000_movies;

select series_title, released_year, certificate, genre, imdb_rating 
from top_1000_movies
where certificate = 'U'
order by imdb_rating
desc
limit 10;


select * from top_1000_movies
WHERE genre like 'Mystery%'
ORDER BY imdb_rating
DESC;


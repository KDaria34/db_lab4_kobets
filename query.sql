SELECT genre_type, COUNT(name) AS film_count
FROM title_genre
GROUP BY genre_type;

SELECT name
FROM Title
WHERE title_type = 'MOVIE';

SELECT release_year, COUNT(name) AS film_count
FROM Title
GROUP BY release_year
ORDER BY release_year;

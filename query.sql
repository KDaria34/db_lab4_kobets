SELECT Title.name
FROM Title
JOIN title_genre ON Title.name = title_genre.name
JOIN Genre ON title_genre.genre_type = Genre.genre_type
WHERE Genre.genre_type = 'romance' AND Title.title_type = 'MOVIE';

SELECT t.name
FROM Title t
JOIN title_genre tg ON t.name = tg.name
GROUP BY t.name
HAVING COUNT(tg.genre_type) = 2;

SELECT tg.genre_type, COUNT(tg.name) AS film_count
FROM title_genre tg
GROUP BY tg.genre_type
ORDER BY film_count DESC
FETCH FIRST 1 ROW ONLY;

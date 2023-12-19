INSERT INTO Title(name, title_type, release_year)
VALUES('Taxi Driver', 'MOVIE', '1976');
INSERT INTO Title(name, title_type, release_year)
VALUES('Monty Python and the Holy Grail', 'MOVIE', '1975');
INSERT INTO Title(name, title_type, release_year)
VALUES('The Exorcist', 'MOVIE', '1973');
INSERT INTO Title(name, title_type, release_year)
VALUES('Monty Pythons Flying Circus', 'SHOW', '1969');
INSERT INTO Title(name, title_type, release_year)
VALUES('Five Came Back: The Reference Films', 'SHOW', '1945');
INSERT INTO Title(name, title_type, release_year)
VALUES('The Blue Lagoon', 'MOVIE', '1980');
INSERT INTO Title(name, title_type, release_year)
VALUES('Alexandria… Why?', 'MOVIE', '1979');
INSERT INTO Title(name, title_type, release_year)
VALUES('No Longer Kids', 'MOVIE', '1979');

INSERT INTO Genre(genre_type)
VALUES('romance');
INSERT INTO Genre(genre_type)
VALUES('horror');
INSERT INTO Genre(genre_type)
VALUES('crime');
INSERT INTO Genre(genre_type)
VALUES('drama');
INSERT INTO Genre(genre_type)
VALUES('documentation');
INSERT INTO Genre(genre_type)
VALUES('comedy');
INSERT INTO Genre(genre_type)
VALUES('fantasy');


INSERT INTO title_genre(name, genre_type)
VALUES('Taxi Driver', 'crime');
INSERT INTO title_genre(name, genre_type)
VALUES('Taxi Driver', 'drama');
INSERT INTO title_genre(name, genre_type)
VALUES('Monty Python and the Holy Grail', 'comedy');
INSERT INTO title_genre(name, genre_type)
VALUES('Monty Python and the Holy Grail', 'fantasy');
INSERT INTO title_genre(name, genre_type)
VALUES('The Exorcist', 'horror');
INSERT INTO title_genre(name, genre_type)
VALUES('Monty Pythons Flying Circus', 'comedy');
INSERT INTO title_genre(name, genre_type)
VALUES('Monty Pythons Flying Circus', 'fantasy');
INSERT INTO title_genre(name, genre_type)
VALUES('Five Came Back: The Reference Films', 'documentation');
INSERT INTO title_genre(name, genre_type)
VALUES('The Blue Lagoon', 'romance');
INSERT INTO title_genre(name, genre_type)
VALUES('The Blue Lagoon', 'drama');
INSERT INTO title_genre(name, genre_type)
VALUES('Alexandria… Why?', 'drama');
INSERT INTO title_genre(name, genre_type)
VALUES('No Longer Kids', 'drama');
INSERT INTO title_genre(name, genre_type)
VALUES('No Longer Kids', 'comedy');

CREATE TABLE Title
(
  name VARCHAR2(100) NOT NULL, 
  title_type VARCHAR2(50) NOT NULL, 
  release_year VARCHAR2(50) NOT NULL,
  PRIMARY KEY (name)
);

CREATE TABLE Genre
(
  genre_type VARCHAR2(50) NOT NULL, 
  PRIMARY KEY (genre_type)
);

CREATE TABLE title_genre
(
  name VARCHAR2(100) NOT NULL, 
  genre_type VARCHAR2(50) NOT NULL, 
  FOREIGN KEY (name) REFERENCES Title(name),
  FOREIGN KEY (genre_type) REFERENCES Genre(genre_type)
);

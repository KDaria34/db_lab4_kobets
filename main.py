import psycopg2

username = 'postgres'
password = '123456'
database = 'lab3'
host = 'localhost'
port = '5433'

query_1 = '''
SELECT Title.name
FROM Title
JOIN title_genre ON Title.name = title_genre.name
JOIN Genre ON title_genre.genre_type = Genre.genre_type
WHERE Genre.genre_type = 'romance' AND Title.title_type = 'MOVIE';
'''
query_2 = '''
SELECT t.name
FROM Title t
JOIN title_genre tg ON t.name = tg.name
GROUP BY t.name
HAVING COUNT(tg.genre_type) = 2;

'''

query_3 = '''
SELECT tg.genre_type, COUNT(tg.name) AS film_count
FROM title_genre tg
GROUP BY tg.genre_type
ORDER BY film_count DESC
FETCH FIRST 1 ROW ONLY;

'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:
                       
    print ("Database opened successfully")
    cur = conn.cursor()

    print('1. Вивести усі фільми жанру романтика \n')
    cur.execute(query_1)

    for row in cur:
        print(row)

    print('2. Вивести усі фільми з більш ніж одним жанром \n')
    cur.execute(query_2)

    for row in cur:
        print(row)

    print('3. Вивести жанр з найбільшою кількістю фільмів  \n')
    cur.execute(query_3)

    for row in cur:
        print(row)

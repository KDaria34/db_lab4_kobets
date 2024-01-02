import psycopg2

username = 'postgres'
password = '123456'
database = 'lab3.2'
host = 'localhost'
port = '5433'

query_1 = '''
SELECT genre_type, COUNT(name) AS film_count
FROM title_genre
GROUP BY genre_type;
'''
query_2 = '''
SELECT title_type, COUNT(name) AS film_count
FROM Title
GROUP BY title_type;

'''

query_3 = '''
SELECT release_year, COUNT(name) AS film_count
FROM Title
GROUP BY release_year
ORDER BY release_year;

'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:
                       
    print ("Database opened successfully")
    cur = conn.cursor()

    print('1. Виведення кількості фільмів кожного жанру:\n')
    cur.execute(query_1)

    for row in cur:
        print(row)

    print('2. Виведення назв фільмів, які є типами "MOVIE": \n')
    cur.execute(query_2)

    for row in cur:
        print(row)

    print('3. Виведення залежності фільмів від року:\n')
    cur.execute(query_3)

    for row in cur:
        print(row)

import psycopg2
import matplotlib.pyplot as plt

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

    cur.execute(query_1)

    titles = []

    for row in cur:
        titles.append(row[0])

    figure, bar_ax = plt.subplots()
    bar = bar_ax.bar(titles, [1] * len(titles), label='Total', color='skyblue') 
    bar_ax.bar_label(bar, label_type='center')

    bar_ax.set_xlabel('Назви фільмів')
    bar_ax.set_ylabel('Кількість')
    bar_ax.set_title('Фільми у жанрі "romance" та типі "MOVIE"')

    cur.execute(query_2)

    title_names = []
    counts = []

    for row in cur:
        title_names.append(row[0])
        counts.append(1)  

    figure, pie_ax = plt.subplots()
    pie_ax.pie(counts, labels=title_names, autopct='%1.1f%%', startangle=90, counterclock=False)
    pie_ax.set_title('Частка фільмів з двома жанрами')

    cur.execute(query_3)

    row = cur.fetchone()

    if row is not None:
        genre = row[0]
        film_count = row[1]

    # Create a bar chart
    figure, graph_ax = plt.subplots()
    graph_ax.bar(genre, film_count, color='purple', alpha=0.7)

    # Customize the plot
    graph_ax.set_xlabel('Жанр')
    graph_ax.set_ylabel('Кількість фільмів')
    graph_ax.set_title(f'Графік для жанру з найбільшою кількістю фільмів: {genre}')

mng = plt.get_current_fig_manager()
mng.resize(1400, 600)

plt.show()

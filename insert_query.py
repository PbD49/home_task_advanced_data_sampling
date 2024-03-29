from class_db import DataBase, username, password

db = DataBase('music_db', user=username, password=password, host='127.0.0.1', port='5432')

genres_data = [
    ('Rock',),
    ('Pop',),
    ('Hip-Hop',),
    ('Jazz',)
]

for genre in genres_data:
    db.execute_query("INSERT INTO Genres (name_genres) VALUES (%s)", genre)

artists_data = [
    ('first',),
    ('linkin park',),
    ('ron',),
    ('garry potter',)
]

for artist in artists_data:
    db.execute_query("INSERT INTO Artists (name_artists) VALUES (%s)", artist)

album_data = [
    ('Album1', 2019, 1),
    ('Album2', 2005, 2),
    ('Album3', 2020, 3)
]

for album in album_data:
    db.execute_query("INSERT INTO Albums (name_album, year_of_issue, genre_id) VALUES (%s, %s, %s)", album)

artist_genres_data = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
]

for item in artist_genres_data:
    db.execute_query("INSERT INTO ArtistGenres (artist_id, genre_id) VALUES (%s, %s)", item)

artist_albums_data = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 1),
]

for item in artist_albums_data:
    db.execute_query("INSERT INTO ArtistAlbums (artist_id, album_id) VALUES (%s, %s)", item)

song_data = [
    ('мой батон самый лучший в мире', 2, 1),
    ('my favorite', 22, 1),
    ('Song3', 1, 2),
    ('Song4', 5, 2),
    ('Song5', 3.5, 3),
    ('Song6', 4, 3)
]

for song in song_data:
    db.execute_query("INSERT INTO List_of_songs (name_songs, song_duration, album_id) VALUES (%s, %s, %s)", song)

collection_data = [
    ('Collection1', 2019),
    ('Collection2', 2020),
    ('Collection3', 2045)
]

for collection in collection_data:
    db.execute_query("INSERT INTO Collection (name_collection, year_of_issue) VALUES (%s, %s)", collection)

song_collection_data = [
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 2),
    (5, 3),
    (6, 3)
]

for song_collection in song_collection_data:
    db.execute_query("INSERT INTO SongCollection (song_id, collection_id) VALUES (%s, %s)", song_collection)

from class_db import DataBase, username, password


db = DataBase('music_db', user=username, password=password, host='127.0.0.1', port='5432')

db.execute_query('''DROP TABLE IF EXISTS 
                        Genres, Artists, Albums, ArtistGenres, 
                        ArtistAlbums, List_of_songs, Collection,
                        SongCollection
''')

db.execute_query('''
    CREATE TABLE IF NOT EXISTS Genres (
        id SERIAL PRIMARY KEY,
        name_genres TEXT UNIQUE
    )
''')

db.execute_query('''
    CREATE TABLE IF NOT EXISTS Artists (
        id SERIAL PRIMARY KEY,
        name_artists TEXT
    )
''')

db.execute_query('''
    CREATE TABLE IF NOT EXISTS Albums (
        id SERIAL PRIMARY KEY,
        name_album TEXT,
        year_of_issue INTEGER CHECK (year_of_issue >= 1900),
        genre_id INTEGER,
        FOREIGN KEY (genre_id) REFERENCES Genres(id)
    )
''')

db.execute_query('''
    CREATE TABLE IF NOT EXISTS ArtistGenres (
        artist_id INTEGER,
        genre_id INTEGER,
        PRIMARY KEY (artist_id, genre_id),
        FOREIGN KEY (artist_id) REFERENCES Artists(id),
        FOREIGN KEY (genre_id) REFERENCES Genres(id)
    )
''')

db.execute_query('''
    CREATE TABLE IF NOT EXISTS ArtistAlbums (
        artist_id SERIAL,
        album_id INTEGER,
        PRIMARY KEY (artist_id, album_id),
        FOREIGN KEY (artist_id) REFERENCES Artists(id),
        FOREIGN KEY (album_id) REFERENCES Albums(id)
    )
''')

db.execute_query('''
    CREATE TABLE IF NOT EXISTS List_of_songs (
        id SERIAL PRIMARY KEY,
        name_songs TEXT,
        song_duration INTEGER CHECK (song_duration > 0),
        album_id INTEGER,
        FOREIGN KEY (album_id) REFERENCES Albums(id)
    )
''')

db.execute_query('''
    CREATE TABLE IF NOT EXISTS Collection (
        id SERIAL PRIMARY KEY,
        name_collection TEXT,
        year_of_issue INTEGER CHECK (year_of_issue >= 1900)
    )
''')

db.execute_query('''
    CREATE TABLE IF NOT EXISTS SongCollection (
        song_id INTEGER,
        collection_id INTEGER,
        PRIMARY KEY (song_id, collection_id),
        FOREIGN KEY (song_id) REFERENCES List_of_songs(id),
        FOREIGN KEY (collection_id) REFERENCES Collection(id)
    )
''')

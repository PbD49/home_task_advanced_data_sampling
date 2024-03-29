from class_db import DataBase, username, password
from pprint import pprint

db = DataBase('music_db', user=username, password=password, host='127.0.0.1', port='5432')


pprint(db.fetch_all('''SELECT name_songs, song_duration
FROM List_of_songs
WHERE song_duration = (SELECT MAX(song_duration) FROM List_of_songs);'''))

pprint(db.fetch_all('''SELECT name_songs, song_duration
FROM List_of_songs
WHERE song_duration >= 3.5;
'''))

pprint(db.fetch_all('''SELECT name_collection
FROM Collection
WHERE year_of_issue BETWEEN 2018 AND 2020;
'''))

pprint(db.fetch_all('''SELECT name_artists
FROM Artists
WHERE name_artists NOT LIKE '% %';
'''))

pprint(db.fetch_all('''SELECT name_songs
FROM List_of_songs
WHERE name_songs ILIKE '%мой%' OR name_songs ILIKE '%my%';
'''))

pprint(db.fetch_all('''SELECT g.name_genres, COUNT(ag.artist_id) AS artist_count
FROM ArtistGenres ag
JOIN Genres g ON ag.genre_id = g.id
JOIN Artists a ON ag.artist_id = a.id
GROUP BY g.name_genres;
'''))

pprint(db.fetch_all('''SELECT COUNT(ls.id) AS track_count
FROM List_of_songs ls
JOIN Albums a ON ls.album_id = a.id
WHERE a.year_of_issue BETWEEN 2019 AND 2020;
'''))

pprint(db.fetch_all('''SELECT a.name_artists
FROM Artists a
LEFT JOIN ArtistAlbums aa ON a.id = aa.artist_id
LEFT JOIN Albums al ON aa.album_id = al.id
WHERE al.year_of_issue != 2020 OR al.year_of_issue IS NULL;
'''))

pprint(db.fetch_all('''SELECT c.name_collection
FROM Collection c
JOIN SongCollection sc ON c.id = sc.collection_id
JOIN List_of_songs ls ON sc.song_id = ls.id
JOIN ArtistAlbums aa ON ls.album_id = aa.album_id
WHERE aa.artist_id = 1;
'''))

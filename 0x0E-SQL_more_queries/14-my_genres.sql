-- Script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- The tv_shows table contains only one record where title = Dexter
SELECT name FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = genre_id
LEFT JOIN tv_shows ON tv_shows.id = show_id
WHERE title = "Dexter"
ORDER BY name ASC;

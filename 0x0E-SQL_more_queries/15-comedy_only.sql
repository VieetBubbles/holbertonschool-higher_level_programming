-- Script that lists all Comedy shows in the database hbtn_0d_tvshows
-- The tv_genres table contains only one record where name = Comedy
SELECT title FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = genre_id
LEFT JOIN tv_shows ON tv_shows.id = show_id
WHERE name = "Comedy"
ORDER BY title ASC;

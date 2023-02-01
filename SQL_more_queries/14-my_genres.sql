-- hii
SELECT tv_genres.name as name
FROM tv_genres INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres genre_id
FROM tv_show_genres INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
ORDER BY name ASC;

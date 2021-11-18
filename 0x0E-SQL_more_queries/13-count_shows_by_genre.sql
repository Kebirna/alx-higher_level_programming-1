-- lists all genres from hbnt_0d_shows
SELECT tv_genres.name, COUNT(*) AS num
FROM tv_genres
GROUP BY tv_shows.name
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY num DESC;

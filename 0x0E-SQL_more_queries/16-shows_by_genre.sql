-- listing show by genre
SELECT s.title, g.name
FROM tv_shows s
LEFT JOIN tv_show_genres m on s.id = m.show_id
LEFT JOIN tv_genres g on m.genre_id = g.id
ORDER BY s.title ASC;

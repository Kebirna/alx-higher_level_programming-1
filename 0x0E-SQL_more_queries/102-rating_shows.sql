-- lsts all show from hbtn_0d_tvshows_rate
SELECT title, SUM(rate) AS rate
FROM tv_shows as ts
INNER JOIN tv_show_ratings AS r
ON ts.id = r.show_id
GROUP BY title
ORDER BY rate DESC;

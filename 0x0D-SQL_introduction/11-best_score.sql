-- Lists all records with scores of at least 10
-- Display both scores and name
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY score DESC;

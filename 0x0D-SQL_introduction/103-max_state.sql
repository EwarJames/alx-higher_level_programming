-- Script that displays the max temperatures of each state
-- Ordered by state name
SELECT `state`, AVG(`value`) As `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;

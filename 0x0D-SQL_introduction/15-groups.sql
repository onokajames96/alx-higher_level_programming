-- A script that lists the number of records with.
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score DESC;

-- SQL Member Count
-- Your table: maintable_WHSJI

-- MySQL version: 8.0.23

-- In this MySQL challenge, your query should return the names of the people who are reported to (excluding null values), 
-- the number of members that report to them, and the average age of those members as an integer. 
-- The rows should be ordered by the names in alphabetical order. 
-- Your output should look like the following table.

-- https://coderbytestaticimages.s3.amazonaws.com/editor/challenges/ascii_member_count.png

SELECT ReportsTo,COUNT(*) AS Members,ROUND(AVG(Age)) AS 'Average Age'
FROM maintable_WHSJI WHERE ReportsTo IS NOT NULL
GROUP BY ReportsTo ORDER BY ReportsTo ASC
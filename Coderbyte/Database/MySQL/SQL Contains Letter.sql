-- SQL Contains Letter
-- Your table: maintable_IMWPO

-- MySQL version: 8.0.23

-- In this MySQL challenge, your query should return the number of rows from your table where FirstName contains "e" 
-- and LastName has more than 5 characters. Your output should look like the following table.

/* write your SQL query below */

SELECT COUNT(*)
FROM maintable_IMWPO
WHERE FirstName LIKE '%e%' AND LENGTH(LastName) > 5;
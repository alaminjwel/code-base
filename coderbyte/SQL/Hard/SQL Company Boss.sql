-- SQL Company Boss
-- Your table: maintable_T37SJ

-- MySQL version: 8.0.23

-- In this MySQL challenge, your query should return all the people who report to either Jenny Richards or have a NULL value in ReportsTo. 
-- The rows should be ordered by Age. Your query should also add a column at the end with a title of Boss Title 
-- where the value is either None or CEO. Your output should look like the following table.


/* write your SQL query below */

SELECT 
    FirstName, LastName, ReportsTo, Position, Age, 
   CASE 
      WHEN ReportsTo=(SELECT CONCAT(FirstName, ' ', LastName) FROM maintable_T37SJ WHERE Position='CEO')
      THEN 'CEO' 
      ELSE 'None' 
   END AS 'Boss Title'
FROM maintable_T37SJ
WHERE ReportsTo = 'Jenny Richards' OR ReportsTo IS NULL 
ORDER BY Age;

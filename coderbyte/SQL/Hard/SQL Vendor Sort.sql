-- SQL Vendor Sort
-- Your table: maintable_GIUWL

-- MySQL version: 8.0.23

-- In this MySQL challenge, your query should return the vendor information along with the values from the table cb_vendorinformation. 
-- You should combine the values of the two tables based on the GroupID column.
-- The final query should consolidate the rows to be grouped by FirstName, 
-- and a Count column should be added at the end that adds up the number of times that person shows up in the table. 
-- The output table should be sorted by the Count column in ascending order and then sorted by CompanyName in alphabetical order. 
-- Your output should look like the following table.
-- https://coderbytestaticimages.s3.amazonaws.com/editor/challenges/ascii_vendor_sort.png


SELECT 
t1.GroupID,
t1.FirstName,
t1.LastName,
t1.Job,
t1.ExternalID,
t2.CompanyName,
COUNT(t1.GroupID) AS Count 
FROM maintable_GIUWL t1
LEFT JOIN cb_vendorinformation t2 ON t1.GroupID=t2.GroupID
GROUP BY t1.FirstName ORDER BY Count,CompanyName
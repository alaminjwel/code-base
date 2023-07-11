-- SQL Vendor Join
-- Your table: maintable_MH65W

-- MySQL version: 8.0.23

-- In this MySQL challenge, your query should return the vendor information along with the values from the table cb_vendorinformation. 
-- You should combine the values of the two tables based on the GroupID column. 
-- The final query should only print out the GroupID, CompanyName, and final count of all rows 
-- that are grouped into each company name under a column titled Count. The output table should be then sorted by the 
-- Count column and then sorted by GroupID so that a higher number appears first.
-- https://coderbytestaticimages.s3.amazonaws.com/editor/challenges/ascii_vendor_join.png

/* write your SQL query below */

SELECT t1.GroupID,t2.CompanyName,COUNT(t1.GroupID) AS Count FROM maintable_MH65W t1
LEFT JOIN cb_vendorinformation t2 ON t1.GroupID=t2.GroupID
GROUP BY t1.GroupID ORDER BY Count,GroupID
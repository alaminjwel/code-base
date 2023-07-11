-- In this MySQL challenge, your query should return the information for the employee with 
-- the third highest salary. Write a query that will find this employee and return that row, 
-- but then replace the DivisionID column with the corresponding DivisionName from the table cb_companydivisions. 
-- You should also replace the ManagerID column with the ManagerName if the ID exists in the table and is not NULL.

-- Your output should look like the following table.
-- ID,Name,DivisionName,ManagerName,Salary

SELECT e.ID, e.Name, d.DivisionName, IFNULL(m.Name, 'N/A') AS ManagerName, e.Salary
FROM maintable_28CP8 e
LEFT JOIN cb_companydivisions d ON e.DivisionID = d.ID
LEFT JOIN maintable_28CP8 m ON e.ManagerID = m.ID
WHERE (
  SELECT COUNT(DISTINCT Salary)
  FROM maintable_28CP8
  WHERE Salary > e.Salary
) = 2
ORDER BY e.Salary DESC
LIMIT 1;

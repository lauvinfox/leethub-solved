# Write your MySQL query statement below
# SELECT x.unique_id, y.name FROM employees y LEFT JOIN EmployeeUNI x ON x.id = y.id;
SELECT  unique_id, name FROM  Employees LEFT OUTER JOIN EmployeeUNI USING (id)
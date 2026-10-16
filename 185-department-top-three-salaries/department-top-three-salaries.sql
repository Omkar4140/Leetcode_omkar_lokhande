-- WITH RankedEmployees AS (
--     SELECT id, name, departmentId, salary,
--            DENSE_RANK() OVER (PARTITION BY DEPARTMENT ORDER BY salary DESC) as sal
--     FROM Employee
-- )
-- SELECT name, employee, salary
-- FROM RankedEmployees;

SELECT d.name AS Department,
        e1.name AS Employee,
        e1.salary AS Salary
FROM Employee e1 INNER JOIN Department d
ON e1.departmentID = d.id
WHERE 3 > (
    SELECT COUNT(DISTINCT(e2.salary))
    FROM Employee e2
    WHERE e2.salary> e1.salary AND
    e2.DepartmentId = e1.DepartmentId
)
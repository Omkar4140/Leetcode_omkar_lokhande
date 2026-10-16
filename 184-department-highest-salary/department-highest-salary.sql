WITH cte AS 
(SELECT e.name AS Employee,
        d.name AS Department,
        e.salary AS Salary,

        MAX(e.salary)OVER(PARTITION BY e.departmentId) as maxSalary
FROM Employee e
LEFT JOIN Department d
ON e.departmentId = d.id)
SELECT Department, Employee, Salary
FROM cte
WHERE salary= maxSalary
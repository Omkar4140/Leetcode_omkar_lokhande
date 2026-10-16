WITH cte AS 
(SELECT e.name AS Employee,
        d.name AS Department,
        e.salary AS Salary,

        DENSE_RANK()OVER(PARTITION BY e.departmentId ORDER BY e.salary DESC) as RK
FROM Employee e
LEFT JOIN Department d
ON e.departmentId = d.id)
SELECT Department, Employee, Salary
FROM cte
WHERE RK =1;
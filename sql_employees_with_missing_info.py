#https://leetcode.com/problems/employees-with-missing-information/description/

SELECT T.employee_id
from 
(
    select * from Employees LEFT JOIN Salaries USING (employee_id)
    union
    select * from Salaries LEFT JOIN Employees USING (employee_id)
) AS T
where T.salary IS NULL OR T.name IS NULL
order by employee_id;
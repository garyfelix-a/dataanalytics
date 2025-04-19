CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);

select * from employees;
 
INSERT INTO employees (employee_id, name, department, salary) VALUES
(1, 'Alice',   'Sales', 50000),
(2, 'Bob',     'Sales', 60000),
(3, 'Charlie', 'Sales', 45000),
(4, 'David',   'IT',    70000),
(5, 'Eva',     'IT',    80000),
(6, 'Frank',   'IT',    75000);

INSERT INTO employees (employee_id, name, department, salary) VALUES
(7, 'John',   'Sales', 50000),
(8, 'Doe',   'Sales', 45000);



-- Rank employees by salary within each department
SELECT 
	employee_id,
    name,
    department,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY 
    salary DESC) AS rank_in_dept
FROM employees;   

-- Total salary using SUM()
SELECT employee_id, name, salary,
SUM(salary) OVER (ORDER BY salary) AS running_total
FROM employees; 

-- Compare each employee's salary with prev(lag) and next(lead)
SELECT 
	employee_id,
    name,
    salary,
    LAG(salary, 1, 0) OVER (ORDER BY salary) AS prev_salary,
    LEAD(salary) OVER (ORDER BY salary) AS next_salary
FROM employees;
    
-- rank employees by salary within department (with ties)
SELECT employee_id, name, department, salary,
RANK() OVER (PARTITION BY department ORDER BY salary DESC)
AS salary_rank
FROM employees;

SELECT employee_id, name, department, salary,
dense_rank() OVER (ORDER BY salary DESC)
AS salary_rank
FROM employees;

-- NTILE --> Grouping based on something
SELECT
	employee_id,
    name, 
    salary,
    NTILE(3) OVER (ORDER BY salary DESC) AS salary_quartile
FROM employees;


SELECT * FROM EMPLOYEES;

-- practices

SELECT name, department, salary,
	rank() over (partition by department order by salary 
    desc) as rank_in_dept
from employees;

select name, department, salary,
	sum(salary) over (partition by department order by 
    salary) as cumulative_salary
from employees;





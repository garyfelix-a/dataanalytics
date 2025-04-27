use rev_datanalytics;

CREATE TABLE Employees
(
	emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    emp_salary VARCHAR(250)
);

insert into employees 
values
(1, 'Goldberg', '30000'),
(2, 'Rock', '40000'),
(3, 'Cena', '20000');

ALTER TABLE employees
ADD emp_dep VARCHAR(256);

SELECT * FROM employees
ORDER BY emp_salary;

SELECT * FROM employees
ORDER BY emp_salary desc;

SELECT * FROM employees
ORDER BY emp_salary;
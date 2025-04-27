USE REV_DATANALYTICS;

SELECT * FROM EMPLOYEE;

-- Create VIEWS
CREATE VIEW sales_employees AS
SELECT EMP_ID, ENAME, SALARY
FROM EMPLOYEE
WHERE JOB_DESC = 'SALES';

SELECT * FROM sales_employees;

-- ALTER VIEWS
CREATE OR REPLACE VIEW sales_employees AS
SELECT EMP_ID, ENAME, SALARY, HIRE_DATE 
FROM EMPLOYEE
WHERE JOB_DESC = 'SALES';

SELECT * FROM sales_employees;

-- DROP VIEWS
DROP VIEW sales_employees;

-- we can use insert, update or delete statements using views
-- which will reflect in the table alter
-- we are updateing the salary using views 
UPDATE sales_employees
SET salary = salary * 1.50
WHERE EMP_ID = 2;

SELECT * FROM EMPLOYEE; 

create view high_payers AS
select * from employees
where salary > 40000;

create or replace view high_payers as
select * from employees
where salary > 60000;

select * from high_payers;

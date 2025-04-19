SELECT 
	employee_id,
    salary,
    CASE
		WHEN salary > 100000 THEN 'High'
        WHEN salary BETWEEN 50000 AND 100000 THEN 'Medium'
        ELSE 'Low'
	END AS salary_grade
FROM employees;

CREATE TABLE ORDERS(
	OID INT PRIMARY KEY AUTO_INCREMENT,
    O_NAME VARCHAR(100),
    PRORITY VARCHAR(100)
);

SELECT * FROM PRODUCTS;

DELETE FROM PRODUCTS WHERE PRODUCTID = 2;

UPDATE PRODUCTS
SET PRICE = 
CASE 
	WHEN ProductName = 'Product3' THEN PRICE * 2
	WHEN ProductName = 'Product4' THEN PRICE * 0.8
    ELSE PRICE
END;

CREATE TABLE PEOPLE(
	ID INT PRIMARY KEY AUTO_INCREMENT,
    NAME VARCHAR(100),
    AGE INT,
    PLACE VARCHAR(256)
);

INSERT INTO PEOPLE VALUES
(1,'Alice', 23, 'USA'),
(2,'Bob', 33, 'UK'),
(3,'John', 63, 'India'),
(4,'Steve', 15, 'Australia');

select * from people;

SELECT NAME, AGE,
CASE 
	WHEN AGE < 18 THEN 'MINOR'
    WHEN AGE BETWEEN 18 AND 59 THEN 'ADULT'
    ELSE 'SENIOR'
END AS age_group
FROM PEOPLE;

CREATE TABLE STUDENT(
	ID INT PRIMARY KEY,
    NAME VARCHAR(100),
    AGE INT,
    MARKS INT,
    PLACE VARCHAR(256)
);

INSERT INTO STUDENT VALUES
(1,'Alice', 23, 95, 'USA'),
(2,'Bob', 33, 75, 'UK'),
(3,'John', 63, 60, 'India'),
(4,'Steve', 15, 40, 'Australia');

SELECT * FROM STUDENT;

UPDATE student
SET GRADE = 
CASE 
	WHEN marks >= 90 THEN 'A'
	WHEN marks >= 75 THEN 'B'
	WHEN marks >= 60 THEN 'C'
    ELSE 'D'
END;

SELECT * FROM EMPLOYEES;
EXPLAIN SELECT * FROM EMPLOYEES WHERE DEPARTMENT = 'SALES';

select name, department, 
case 
	when salary > 50000 then "High"
    when salary between 30000 and 50000 then "medium"
    else 'low'
end as salary_measure
from employees;
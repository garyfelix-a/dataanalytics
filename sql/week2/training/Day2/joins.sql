use rev_datanalytics;

CREATE TABLE Customerstable (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    ContactName VARCHAR(100),
    Country VARCHAR(50)
);
 
CREATE TABLE Orderstable (
    OrderID INT PRIMARY KEY,
    OrderDate DATE,
    CustomerID INT,
    Amount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customerstable(CustomerID)
);
 
INSERT INTO Customerstable (CustomerID, CustomerName, ContactName, Country) VALUES
(1, 'John Doe', 'John D.', 'USA'),
(2, 'Jane Smith', 'Jane S.', 'UK'),
(3, 'Alice Brown', 'Alice B.', 'Canada'),
(4, 'Bob Johnson', 'Bob J.', 'Australia');
 
INSERT INTO Orderstable (OrderID, OrderDate, CustomerID, Amount) VALUES
(101, '2024-09-01', 1, 250.00),
(102, '2024-09-05', 2, 300.00),
(103, '2024-09-07', 1, 150.00),
(104, '2024-09-10', 3, 450.00);

select * from Customerstable;

SELECT 
	customerstable.CustomerID,
    customerstable.CustomerName,
    orderstable.OrderID,
    orderstable.OrderDate,
    orderstable.Amount
FROM
	customerstable
INNER JOIN
	orderstable 
ON
	customerstable.CustomerID = orderstable.CustomerID;
    
SELECT 
	customerstable.CustomerID,
    customerstable.CustomerName,
    orderstable.OrderID,
    orderstable.OrderDate,
    orderstable.Amount
FROM
	customerstable
LEFT JOIN
	orderstable 
ON
	customerstable.CustomerID = orderstable.CustomerID;
    
SELECT 
	customerstable.CustomerID,
    customerstable.CustomerName,
    orderstable.OrderID,
    orderstable.OrderDate,
    orderstable.Amount
FROM
	customerstable
RIGHT JOIN
	orderstable 
ON
	customerstable.CustomerID = orderstable.CustomerID;
    
SELECT 
	customerstable.CustomerID,
    customerstable.CustomerName,
    orderstable.OrderID,
    orderstable.OrderDate,
    orderstable.Amount
FROM
	customerstable
JOIN
	orderstable 
ON
	customerstable.CustomerID = orderstable.CustomerID;
    
CREATE TABLE Drinks(
	id INT PRIMARY KEY,
    drinks VARCHAR(200)
);

CREATE TABLE Snacks(
	id INT PRIMARY KEY,
    snacks VARCHAR(200)
);

INSERT INTO DRINKS
VALUES
(1, 'Coke'),
(2, 'Monster');

INSERT INTO Snacks
VALUES
(1, 'Puffs'),
(2, 'Spring Potatoes');

SELECT 
	drinks.id,
    drinks.drinks,
    snacks.snacks
FROM
	Drinks
CROSS JOIN
	Snacks
ON
	drinks.id = snacks.id;
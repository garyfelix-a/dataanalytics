use rev_datanalytics;

CREATE TABLE Products(
	ProductID INT,
    ProductName VARCHAR(20),
    PRICE INT
);

INSERT INTO PRODUCTS(ProductID, ProductName, Price) VALUES
(1, 'Product1', 200), 
(2, 'Product2', 300);

INSERT INTO PRODUCTS(ProductID, ProductName, Price) VALUES
(1, 'Product5', 20), 
(2, 'Product6', 30);

INSERT INTO PRODUCTS VALUES
(3, 'Product3', 100), 
(4, 'Product4', 50);

INSERT INTO PRODUCTS VALUES
(5, 'Product3', 100), 
(6, 'Product4', 50);

SELECT * FROM Products;
-- Query to find Min and Max 
SELECT MIN(PRICE) AS SmallestPrice, ProductID
FROM Products
GROUP BY ProductID; 

SELECT MAX(PRICE) 
FROM Products;

-- Avg
SELECT AVG(PRICE) AS AveragePrice, ProductID
FROM Products
GROUP BY ProductId;

COUNT 
SELECT COUNT(*) AS NumberOfCols
FROM Products;

-- count product whose price is greater than or lesser than
SELECT COUNT(ProductID) FROM Products
WHERE PRICE < 100;

-- Distinct --> to remove duplicates
SELECT COUNT(DISTINCT Price)
FROM Products; 

-- Sum function to get total value
SELECT SUM(PRICE)
FROM Products; 




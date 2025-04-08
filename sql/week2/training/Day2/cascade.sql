USE rev_datanalytics;


-- CASCADE IS USED, IF WE DELETE OR UPDATE IN MAIN TABLE, IT WILL
-- REFLECT IN THE FOREIGN KEY TABLE ALSO.  
CREATE TABLE customer(
	customer_id INT PRIMARY KEY,
    Name VARCHAR(100)
);

CREATE TABLE Orders(
	order_id INT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(100),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
    ON DELETE CASCADE 
);

-- INSERT INTO CUSTOMER
INSERT INTO Customer
VALUES
(3, 'Stone Cold'),
(4, 'Dave Bautista');

-- insert into orders
INSERT INTO orders VALUES
(104, 3, 'Gloves'),
(105, 3, 'Knee Pads'),
(106, 4, 'Punching Bag');

SELECT * FROM Customer;
SELECT * FROM Orders;

DELETE FROM Customer WHERE Customer_id = 1;  
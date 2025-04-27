use rev_datanalytics;

CREATE TABLE ordertable(
	order_id INT PRIMARY KEY NOT NULL,
    customer_id INT, 
    order_date DATE, 
    amount DECIMAL(10, 2),
    status VARCHAR(20)
);

INSERT INTO ordertable values
(1, 101, '2025-01-23', 102.40, 'Completed'),
(2, 102, '2025-02-13', 102.40, 'Cancelled'),
(3, 103, '2025-01-02', 102.40, 'Completed'),
(4, 104, '2025-02-26', 102.40, 'Cancelled');

create table producttable(
	product_id INT PRIMARY KEY NOT NULL,
    category varchar(50),
    name varchar(100),
    price decimal(10, 2),
    stock_quantity INT
);

INSERT INTO producttable values
(1, 'Electronics', 'Laptop', 10202.22, 20),
(2, 'Electronics', 'Phone', 2202.50, 10),
(3, 'Clothing', 'T-Shirt', 10202.00, 5),
(4, 'Home', 'Toaster', 202.12, 2);

select * from ordertable;

-- count orders
SELECT customer_id, count(*) as order_count
from ordertable
group by customer_id;

select customer_id, order_date, status, count(*) as count
from ordertable
group by customer_id, order_date, status;

-- having clause
select customer_id, count(*) as count
from ordertable
group by customer_id
having count(*) < 2;
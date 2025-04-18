-- DELIMITER //
-- CREATE PROCEDURE GETALLUSERS()
-- BEGIN
-- 	SELECT * FROM USERS;
-- END;
-- //

-- CALL GETALLUSERS()

-- DELIMITER //

-- CREATE PROCEDURE GETPRODUCTS(IN ID INT)
-- BEGIN
-- 	SELECT PRODUCTID, PRODUCTNAME FROM PRODUCTS
--     WHERE PRODUCTID = ID;
-- END;
-- //

-- CALL GETPRODUCTS(2)


DELIMITER //
CREATE PROCEDURE GETUSERDETAILS(IN UID INT, 
OUT username VARCHAR(50))
BEGIN
	SELECT UserName INTO username FROM USERS WHERE UserId = UID;
END //
DELIMITER ;
SET @username = '';
CALL GETUSERDETAILS(1, @username);
SELECT @username;


DELIMITER //
CREATE PROCEDURE GETPRODUCTSNAME(IN PID INT, 
OUT PName VARCHAR(50))
BEGIN
	SELECT ProductName INTO PName 
    FROM PRODUCTS
    WHERE ProductID = PID;
END //
DELIMITER ;
SET @productname = '';
CALL GETPRODUCTSNAME(2, @productname);
SELECT @productname; 

SELECT * FROM PRODUCTS;


DELIMITER //
CREATE PROCEDURE PRINTPRODUCTNAME(IN PID INT, 
OUT pname VARCHAR(50))
BEGIN
	SELECT ProductName INTO pname FROM PRODUCTS 
    WHERE ProductID = PID;
END //
DELIMITER ;
SET @productname = '';
CALL PRINTPRODUCTNAME(7, @productname);
SELECT @productname;



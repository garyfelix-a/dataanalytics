DELIMITER //

CREATE FUNCTION CalculateRectangleArea(length FLOAT, 
width FLOAT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
	RETURN length * width;
END //

DELIMITER ;

SELECT CalculateRectangleArea(5.5, 2.3) AS Areas;


-- deterministic function always returns the same results
-- if given the same input values.


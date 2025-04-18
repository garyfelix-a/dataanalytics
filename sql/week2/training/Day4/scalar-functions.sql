-- SCALAR FUNCTIONS
-- if we have only one input to perform operations, we'll use this
-- used for output formatting. 

SELECT ucase("randy ortan") AS UPPERCASE_STRING;

SELECT LCASE("RANDY ORTAN") AS LOWERCASE_STRING;

SELECT MID("RANDY ORTAN", 4, 7) AS SUBSTRING;

SELECT LENGTH("RANDY ORTAN") AS STRING_LENGTH;

SELECT ROUND(1234.23132, 2) AS ROUND_VALUE;

SELECT NOW() AS CURRENT_DATE_TIME;

SELECT FORMAT(1234.1234, 2) AS FORMAT_NUMBER;

SELECT ORDERID, ROUND(AMOUNT) AS ROUND_PRICE FROM ORDERSTABLE;
SELECT * FROM PRODUCTS;
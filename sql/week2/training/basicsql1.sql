create database rev_datanalytics;

use rev_datanalytics;

CREATE TABLE Persons(
	PersonId int,
    FirstName varchar(255),
    LastName varchar(255),
    Address varchar(255),
    City varchar(255)
);

INSERT INTO Persons VALUES
(1, "Randy", "Ortan", "USA","Knoxville"),
(2, "John", "Doe", "India", "Chennai"),
(3, "Bob", "Marley", "Jamaica", "Nine Mile");

SELECT * FROM Persons;

DELETE FROM Persons WHERE PersonId = 3;



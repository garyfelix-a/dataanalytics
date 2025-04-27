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
UPDATE Persons SET LastName = "Cena" WHERE PersonId = 2;


CREATE TABLE Users(
	UserId INT AUTO_INCREMENT PRIMARY KEY,
    UserName VARCHAR(255) UNIQUE NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    PasswordHash VARCHAR(255) NOT NULL,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    CreatedAt DATETIME DEFAULT current_timestamp,
    LastLogin DATETIME,
    Status ENUM('Active', 'Inactive', 'Suspended') DEFAULT 'Active',
    INDEX (Email)
);

INSERT INTO Users(UserName, Email, PasswordHash, 
FirstName, LastName, DateOfBirth, LastLogin, Status)
VALUES (
'steve_16', 'steve_austin@test.com', 'hashed_password', 
'Steve', 'Austin', '1983-03-20', NOW(), 'Active'
);

INSERT INTO Users(UserName, Email, PasswordHash, 
FirstName, LastName, DateOfBirth, LastLogin, Status)
VALUES (
'rohit_45', 'hitman@example.com', 'hashed_password', 
'Rohit', 'Sharma', '1980-05-10', NOW(), 'Inactive'
);

SELECT * FROM Users;

CREATE TABLE Students(
	student_id INT PRIMARY KEY, 
    Name VARCHAR(100),
    Age INT,
    Check(Age>18)
);

INSERT INTO Students(Student_id, Name, Age) VALUES
(1, 'Mark Antony', 19),
(2, 'Kevin', 20);

SELECT * FROM Students;

CREATE TABLE Enrollments(
	enrollment_id INT PRIMARY KEY,
    student_id INT, 
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES Students 
    (student_id)
);

INSERT INTO Enrollments(enrollment_id, student_id, course_id)
VALUES (1, 1, 1);
delete from enrollments where enrollment_id = 1;
SELECT * FROM Enrollments;

CREATE TABLE OrderDetails(
	order_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (order_id, product_id)
);

SELECT * FROM OrderDetails;

DROP TABLE Persons; -- Entire table is deleted from DB

TRUNCATE TABLE Persons; -- removes all data from the table




create database employees;
use employees;

CREATE TABLE emp (
    ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Place VARCHAR(50),
    Job VARCHAR(50),
    Grade VARCHAR(2),
    Height INT,
    Weight INT,
    Mark INT,
    Country VARCHAR(50)
);

INSERT INTO emp (ID, Name, Age, Place, Job, Grade, Height, Weight, Mark, Country) VALUES
(1, 'Alice', 25, 'New York', 'Engineer', 'A', 165, 55, 90, 'USA'),
(2, 'Bob', 30, 'London', 'Doctor', 'B', 175, 70, 85, 'UK'),
(3, 'Charlie', 20, 'Paris', 'Artist', 'C', 180, 75, 75, 'France'),
(4, 'David', 18, 'Tokyo', 'Student', 'D', 160, 50, 65, 'Japan'),
(5, 'Emma', 22, 'Sydney', 'Lawyer', 'A', 170, 60, 95, 'Australia'),
(6, 'Frank', 28, 'Berlin', 'Programmer', 'B', 185, 80, 80, 'Germany'),
(7, 'Grace', 19, 'Madrid', 'Athlete', 'C', 155, 45, 70, 'Spain'),
(8, 'Henry', 35, 'Rome', 'Chef', 'D', 190, 85, 60, 'Italy'),
(9, 'Ivy', 21, 'Moscow', 'Scientist', 'A', 168, 58, 92, 'Russia'),
(10, 'Jack', 24, 'Beijing', 'Entrepreneur', 'B', 170, 65, 88, 'China');

-- Retrieve all individuals 
select * from emp;

-- Retrieve individuals who live in UK:
SELECT * FROM emp WHERE Country="UK";

-- Inserting a new individual
INSERT INTO emp (ID, Name, Age, Place, Job, Grade, Height, Weight, Mark, Country) 
VALUES (11, 'John', 29, 'Toronto', 'Consultant', 'B', 180, 75, 85, 'Canada');

-- Retrieve distinct countries from the emp table:
SELECT DISTINCT Country FROM emp;

-- Retrieve distinct jobs from the emp table:
SELECT DISTINCT Job FROM emp;

-- Retrieve individuals who are younger than 25 years old:
SELECT * FROM emp WHERE Age < 25;

-- Retrieve individuals who work as Engineers and have a grade of 'A':
SELECT * FROM emp WHERE Job = 'Engineer' AND Grade = 'A';

-- Retrieve individuals who work as Engineers or have a grade of 'A':
SELECT * FROM emp WHERE Job = 'Lawyer' OR Grade = 'A';

-- Retrieve individuals who are Female or have a height greater than 180 cm:
SELECT * FROM emp WHERE Gender = 'Female' OR Height > 180;

-- Retrieve individuals who work as Engineers or Scientists:
SELECT * FROM emp WHERE Job IN ('Engineer', 'Scientist');

-- Retrieve individuals who have a grade of 'A' or 'B':
SELECT * FROM emp WHERE Grade IN ('A', 'B');

-- Retrieve individuals who are between 20 and 30 years old:
SELECT * FROM emp WHERE Age BETWEEN 20 AND 30;

-- Retrieve individuals who have a height between 170 and 180 cm:
SELECT * FROM emp WHERE Height BETWEEN 170 AND 180;

-- Retrieve individuals who are younger than 25, from Italy, and have a grade of 'A':
SELECT * FROM emp WHERE Age < 25 AND Country = 'Italy' AND Grade = 'A';

-- Retrieve individuals who have a height between 160 and 180 cm and a weight between 50 and 70 kg:
SELECT * FROM MyTable WHERE Height BETWEEN 160 AND 180 AND Weight BETWEEN 50 AND 70;



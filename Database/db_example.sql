CREATE DATABASE company;

 CREATE TABLE department (
 department_name VARCHAR(50) NOT NULL,
 dep_ID SERIAL NOT NULL,
 PRIMARY KEY(department_name, dep_ID));
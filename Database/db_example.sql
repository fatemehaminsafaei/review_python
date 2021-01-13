CREATE DATABASE company;

CREATE TABLE department (
department_name VARCHAR(50) NOT NULL,
dep_ID SERIAL NOT NULL,
PRIMARY KEY(department_name, dep_ID));

CREATE TABLE supervisor(
supervisor_name VARCHAR(100) NOT NULL,
supervisor_numbers INT NOT NULL,
dep_ID VARCHAR(50),
PRIMARY KEY(supervisor_name));

CREATE TABLE employee( employee_number INT NOT NULL,
employee_name VARCHAR(50) NOT NULL ,
employee_id SERIAL NOT NULL UNIQUE ,
prj_id SERIAL,
PRIMARY KEY (employee_number, employee_id));

CREATE TABLE project(project_number INT NOT NULL,
id SERIAL NOT NULL UNIQUE,
name VARCHAR(50) NOT NULL ,
duration INT ,
PRIMARY KEY(project_number, id));

CREATE TABLE emp_workson_prj(hourlysalary INT,
emp SERIAL,
prj SERIAL ,
FOREIGN KEY(emp) REFERENCES employee(employee_id),
FOREIGN KEY (prj) REFERENCES project(id));
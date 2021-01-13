CREATE DATABASE company;

CREATE TABLE department (
department_name VARCHAR(50) NOT NULL,
dep_ID SERIAL NOT NULL,
PRIMARY KEY(department_name, dep_ID));

CREATE TABLE supervisor(
superviser_name VARCHAR(100) NOT NULL,
superviser_numbers INT NOT NULL,
dep_ID VARCHAR(50),
PRIMARY KEY(superviser_name));

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
employee_id SERIAL,
project_number SERIAL);

-- #INSERT row in tables department

INSERT INTO department(department_name,dep_ID) VALUES
('research' , '1');
INSERT INTO department(department_name,dep_ID) VALUES
('python' , '2');
INSERT INTO department(department_name,dep_ID) VALUES
('raact' , '3');
INSERT INTO department(department_name,dep_ID) VALUES
('javascript' , '4');
INSERT INTO department(department_name,dep_ID) VALUES
('php' , '5');

-- #INSERT row in tables supervisor

INSERT INTO supervisor(superviser_name,superviser_numbers,dep_ID)VALUES('aminsafaei1' , '10', '1');
INSERT INTO supervisor(superviser_name,superviser_numbers,dep_ID)VALUES('aminsafaei2' , '11', '2');
INSERT INTO supervisor(superviser_name,superviser_numbers,dep_ID)VALUES('aminsafaei3' , '12', '3');
INSERT INTO supervisor(superviser_name,superviser_numbers,dep_ID)VALUES('aminsafaei4' , '13', '3');
INSERT INTO supervisor(superviser_name,superviser_numbers,dep_ID)VALUES('aminsafaei5' , '14', '5');

-- #INSERT row in tables employee
INSERT INTO employee(employee_number, employee_name, employee_id) VALUES('20' , 'fateme1', '20');
INSERT INTO employee(employee_number, employee_name, employee_id) VALUES('21' , 'fateme2', '21');
INSERT INTO employee(employee_number, employee_name, employee_id) VALUES('22' , 'fateme3', '22');
INSERT INTO employee(employee_number, employee_name, employee_id) VALUES('23' , 'fateme4', '23');
INSERT INTO employee(employee_number, employee_name, employee_id) VALUES('24' , 'fateme5', '24');

-- #INSERT row in tables project
INSERT INTO project(project_number,id, name,duration ) VALUES('30' , '20', 'deeplearning', '12');
INSERT INTO project(project_number,id, name,duration ) VALUES('31' , '21', 'transferlearning', '8');
INSERT INTO project(project_number,id, name,duration ) VALUES('32' , '22', 'website', '15');
INSERT INTO project(project_number,id, name,duration ) VALUES('33' , '23', 'design', '11');
INSERT INTO project(project_number,id, name,duration ) VALUES('34' , '24', 'database', '18');

-- #INSERT row in tables emp_workson_prj
INSERT INTO emp_workson_prj(hourlysalary, employee_id, project_number ) VALUES('5000000', '20' , '30');
INSERT INTO emp_workson_prj(hourlysalary, employee_id, project_number ) VALUES('6000000', '21' , '31');
INSERT INTO emp_workson_prj(hourlysalary, employee_id, project_number ) VALUES('7000000', '22' , '32');
INSERT INTO emp_workson_prj(hourlysalary, employee_id, project_number ) VALUES('8000000', '23' , '33');
INSERT INTO emp_workson_prj(hourlysalary, employee_id, project_number ) VALUES('9000000', '24' , '34');


-- select count of employee's project
SELECT COUNT(*) FROM project INNER JOIN employee ON id=employee_id WHERE employee_name='fateme1';



-- select
SELECT employee_id FROM emp_workson_prj WHERE hourlysalary = (SELECT MAX(hourlysalary) FROM emp_workson_prj);
SELECT hourlysalary  FROM emp_workson_prj WHERE hourlysalary = (SELECT MAX(hourlysalary) FROM emp_workson_prj);


-- join
SELECT name FROM project INNER JOIN employee ON (id = employee_id) WHERE (employee_name= 'fateme3');


SELECT name , sum(project_number) FROM project INNER JOIN employee(employee_name)
GROUP BY name ORDER BY project_number;


-- SELECT
-- 	name,project_number,count(*) FROM project,employee
-- GROUP BY
-- 	project_number,
-- 	name
-- ORDER BY
--     name;

-- employee name with number of projects
SELECT employee_name AS "employee Name",
COUNT(*) AS "Nunmber of project"
FROM project
INNER JOIN employee
ON employee_name = 'fateme3'
GROUP BY project_number, employee_name
ORDER BY employee_name;


-- 5
SELECT name, department FROM
(project INNER JOIN employee ON id=employee_id )
INNER JOIN department ON dep_id=dep_id;

-- 6
SELECT name FROM (project INNER JOIN employee ON id=employee_id )
INNER JOIN supervisor ON dep_id=dep_id WHERE superviser_name='aminsafaei1';
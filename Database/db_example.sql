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
emp SERIAL,
prj SERIAL ,
FOREIGN KEY(emp) REFERENCES employee(employee_id),
FOREIGN KEY (prj) REFERENCES project(id));

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
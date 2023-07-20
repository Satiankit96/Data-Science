DBMS 
These help us manage the large amounts of data 
- Handles security.
- Handles Backups 
- Importting/exporting/changing Data
- Concurency 
- Work with other software utilities. 

1. Operations of a DBMS 
C.R.U.D
CREATE READ UPDATE DELETE 

1. Types of Databases 
a.  Relational Databases (SQL)
- Organise data in one or more tables.
- These use the language.
- Used to define table and structures. 
- SOme of the RDBMS are mySQL, Oracle,Postgre SQL,MariaDB etc.

b.  Non Relational Database 
- Anything that is not relational.
- Data could be in a key-value store. documents, graphs or flexible tables.
- They have there own queries to perform CRUD.  
- Non Relational DB use mongo DB, Dynamo DB, Apache Cassandra, firebase.

___________________________________________________________________________________________________________________________________________________________

Tables - 
- Primary key - This is the specific attribute that is used to uniquely identify an entity in a given table. (Emails, Roll number)
- Surrogate key - This is an primary key that does not exist in the real world. It is created within an organisation to map its entities.(EMP ID)
- Natural Key - This is also a primary key that has a mapping to the real world. (SSN)

- Foreign key - This is a primary key of another table. THese are used to define relationships between tables. 
- Composite key -This is a primary key that needs two or more columns. They need more columns to uniquely identify an entity. 
___________________________________________________________________________________________________________________________________________________________
SQL Basics 
1. popSQL - AN text editor for RDBMS
2. DataTypes 
   - BLOB - Large files 
   - TIMESTAMP
   - DATE
   - INT/(Others that we use )

3. OPerations 
   Note - We need to click the part of the wuery that we want to run. if we delete a table then we have to click the part where we created and it and run it again. 

-- CREATING A TABLE 

CREATE TABLE student (
    Student_id INT,
    Name VARCHAR (20),
    Major VARCHAR (20),
    PRIMARY KEY (Student_id)
);

DESCRIBE student;

-- DROP TABLE student; - Deleting the table 
ALTER TABLE student ADD gpa DECIMAL(3,2);
ALTER TABLE student DROP COLUMN gpa;

-- ADDING CONSTRAINTS 
    Name VARCHAR (20) NOT NULL, - Value cannot be null 
    Major VARCHAR (20) UNIQUE, - Element should be unique 
    Major VARCHAR (20) DEFAULT 'Undecided', - Gives an default entry 

    student_id INT AUTO_INCREMENT, - Data will be auto iuncremented 

UPDATING IN A TABLE 

UPDATE student
SET Major = 'BioChemistry'
WHERE Major = 'Biology' OR Major = 'Chemistry' -> Over here the semi colon is missing so the next lines will be considered the part of this block 



UPDATE student
SET Major = 'BioChemistry'
WHERE Major = 'Biology' OR Major = 'Chemistry';

UPDATE student
SET Major = 'BioChemistry'
WHERE Major = 'Biology' OR Major = 'Chemistry';

Deleting - 

DELETE FROM student
WHERE student_id = 1;

_________________________________________________________________________________________________________________________________________________________
Getting Information from the Database. 

SELECT - This tells us about the column that we need

OPerators 
<> - NOt equal to 

IN - The IN command allows you to specify multiple values in a WHERE clause. The IN operator is a shorthand for multiple OR conditions.SELECT *
FROM student
WHERE Name IN ('Kate','Jack', 'KATY')
ORDER BY major, student_id DESC
LIMIT 5;



Can't drop table: A foreign key constraint fails
METHOD - 1 
SET FOREIGN_KEY_CHECKS=0; 
DROP TABLE lion.employee;
DROP TABLE lion.branch;
SET FOREIGN_KEY_CHECKS=1;

METHOD 2 
SELECT * 
FROM information_schema.KEY_COLUMN_USAGE 
WHERE REFERENCED_TABLE_NAME = 'lion.employee';
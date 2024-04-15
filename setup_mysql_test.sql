-- write a script to setup a MySQL server for the project
-- create test database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
-- set password for the user
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
-- grant privileges to the user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- grant select privileges to user on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- flush privileges
FLUSH PRIVILEGES;
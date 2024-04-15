-- write a script to setup a MySQL server for the project
-- create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- set password for the user
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- grant privileges to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- grant select privileges to user on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- flush privileges
FLUSH PRIVILEGES;
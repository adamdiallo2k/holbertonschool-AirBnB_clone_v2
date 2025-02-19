-- Script that prepares a MySQL server for the project:
-- Creates the database hbnb_test_db and the user hbnb_test
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
DROP USER IF EXISTS hbnb_test@localhost;
FLUSH PRIVILEGES;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
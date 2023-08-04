-- Script that prepares a MySQL server for the project:
-- Creates the database hbnb_dev_db and the user hbnb_dev
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
DROP USER IF EXISTS hbnb_test@localhost;
FLUSH PRIVILEGES;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
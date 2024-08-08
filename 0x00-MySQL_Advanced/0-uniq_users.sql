-- Create users table
-- This script creates a table named users with id, email, and name attributes.
-- The id is an auto-incrementing integer that is the primary key.
-- The email is a string with a maximum of 255 characters, it is unique and cannot be null.
-- The name is a string with a maximum of 255 characters.
-- If the table already exists, the script will not fail.

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (id)
);

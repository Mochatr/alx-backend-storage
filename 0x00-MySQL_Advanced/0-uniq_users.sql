-- This script creates a table named 'users' if it does not already exist
-- It includes columns for id, email and name with appropriate constraints

CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


# MySQL Advanced

This repository contains advanced SQL scripts and tasks demonstrating the implementation of various SQL techniques and optimizations using MySQL. The project is structured to enhance understanding of advanced SQL concepts, especially focusing on MySQL functionalities.

## Concepts

This project encompasses a thorough examination of the following advanced SQL concept:

- **Advanced SQL**

## Resources

To prepare for this project, the following resources are recommended:

- [MySQL cheatsheet](https://devhints.io/mysql)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.liquidweb.com/kb/mysql-optimization-how-to-leverage-mysql-database-indexing/)
- [Stored Procedure](https://www.w3resource.com/mysql/mysql-procedure.php)
- [Triggers](https://www.w3resource.com/mysql/mysql-triggers.php)
- [Views](https://www.w3resource.com/mysql/mysql-views.php)
- [Functions and Operators](https://dev.mysql.com/doc/refman/5.7/en/functions.html)
- [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/5.7/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/5.7/en/create-view.html)

## Learning Objectives

By the end of this project, you should be able to explain and demonstrate the following without external resources:

### General

- How to create tables with constraints
- How to optimize queries by adding indexes
- Implementation and usage of stored procedures and functions in MySQL
- Implementation and usage of views in MySQL
- Implementation and usage of triggers in MySQL

## Requirements

### General

- All scripts are to be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30).
- Every file must end with a new line.
- Each SQL query must include a comment explaining its purpose.
- All SQL keywords should be in uppercase (e.g., SELECT, WHERE).
- A `README.md` file, at the root of the project folder, is mandatory.
- The length of your files will be tested using `wc`.

## Setup Instructions

### Use Container-On-Demand

- Request an Ubuntu 18.04 container with Python 3.7.
- Connect via SSH or through the WebTerminal.
- Start MySQL with the command: `$ service mysql start`

### Importing a SQL Dump

To import a SQL dump, use the following commands:

```bash
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows


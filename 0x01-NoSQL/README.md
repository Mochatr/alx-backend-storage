# NoSQL Project

## Introduction

This project explores NoSQL databases, focusing primarily on MongoDB. The goal is to understand the fundamentals of NoSQL databases, including their types, benefits, and operations such as querying, inserting, updating, and deleting information.

## Resources

### Reading and Tutorials
- [NoSQL Databases Explained](https://riak.com/resources/nosql-databases/)
- [What is NoSQL?](https://www.youtube.com/watch?v=qUV2j3XBRHc)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://www.youtube.com/watch?v=E-1xI85Zog8)
- [MongoDB Tutorial 2: Insert, Update, Remove, Query](https://www.youtube.com/watch?v=CB9G5Dvv-EE)
- [Aggregation](https://www.mongodb.com/docs/manual/aggregation/)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [mongo Shell Methods](https://www.mongodb.com/docs/manual/reference/method/)
- [Mongosh](https://www.mongodb.com/docs/mongodb-shell/#mongodb-binary-bin.mongosh)

## Learning Objectives

### General
After completing this project, you should be able to explain the following without assistance:
- What NoSQL means
- The difference between SQL and NoSQL databases
- What ACID refers to in databases
- What document storage is
- The various types of NoSQL databases
- The benefits of using NoSQL databases
- How to perform CRUD operations in NoSQL databases
- How to use MongoDB effectively

## Requirements

### MongoDB Command File
- All command files must run on Ubuntu 18.04 LTS with MongoDB version 4.2.
- Files must end with a newline.
- The first line of all command files should be a comment (e.g., `// my comment`).

### Python Scripts
- Scripts must run with Python 3.7 and PyMongo 3.10 on Ubuntu 18.04 LTS.
- Files must end with a newline.
- The first line of all Python files must be `#!/usr/bin/env python3`.
- Follow the pycodestyle (version 2.5.*).
- Use documentation strings for modules and functions.
- Prevent scripts from executing when imported using `if __name__ == "__main__":`.

## More Info

### Installation of MongoDB 4.2 on Ubuntu 18.04
Follow these steps to install MongoDB:

```bash
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
$ sudo service mongod status
$ mongo --version
$ pip3 install pymongo

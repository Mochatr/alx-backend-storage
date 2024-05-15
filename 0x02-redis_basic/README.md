# 0x02. Redis Basic

![Redis](image/redis_image.png)

This project aims to explore the basics of using Redis with Python. Through this project, learners will understand how to utilize Redis for fundamental operations and as a simple caching solution.

## Resources

- [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)
- [Redis commands](https://redis.io/docs/latest/commands/)
- [Redis python client](https://redis-py.readthedocs.io/en/stable/)
- [How to Use Redis With Python](https://realpython.com/python-redis/)

## Learning Objectives

- Understand how to use Redis for basic operations.
- Learn how to implement Redis as a simple caching solution.

## Requirements

- All code must be run on Ubuntu 18.04 LTS using Python 3.7.
- Every file should end with a new line.
- A README.md file, at the root of the folder of the project, is mandatory.
- The first line of all your Python files should be exactly `#!/usr/bin/env python3`.
- Your code should conform to the pycodestyle (version 2.5).
- All modules, classes, and functions/methods must include documentation. Use the following commands to check:
  - `python3 -c 'print(__import__("my_module").__doc__)'`
  - `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
  - `python3 -c 'print(__import__("my_module").my_function.__doc__)'`
  - `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
- Documentation must consist of real sentences explaining the purpose of the module, class, or method.
- All functions and coroutines must be type-annotated.

## Setup and Installation

### Install Redis on Ubuntu 18.04

```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf


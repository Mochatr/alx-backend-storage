# 0x02. Redis Basic

![Redis](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/1/40eab4627f1bea7dfe5e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240515%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240515T113417Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8a3870d148da88392dfc0af2d17b2ef5a7681c11654344f790e3050eb98bc595)

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


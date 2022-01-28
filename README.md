# Welcome to the AirBnB clone project!

---

 ## Table of Contents
* [Introduction](#Introduction)
  * The console
* [Project Tasks](#Project-Tasks)
   * Mandatory Tasks
   * Advanced Tasks
* [Authors](#Authors)

## Introduction
This is a clone of the [Airbnb](https://airbnb.com) website, from the backend to the frontend.  
The project consist of the following parts:  
1. Bulding the console to create a data model and manage data objects. Also store and persist them to a **JSON** file, essentially constituting a storage engine.  
2. The static frontend using **HTML/CSS** and a web template for the objects.  
3. **MySQL** database to replace the file storage engine and map the data models to tables in the database by using an **ORM**.  
4. Creating a templating web framework by building a flask based python server that serve the static frontend with objects from the database or file storage engine.  
5. Creating a **RESTful** API using flask for manipulating objects from the frontend.  
6. Making the website dynamic by using **JS** and load objects using the REST API. 

### The console
The console is written in python using the [cmd](https://docs.python.org/3/library/cmd.html) module. It operates in interactive and non-interactive modes.  

The console works like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
* All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`

![image](https://user-images.githubusercontent.com/88429426/151574529-6ad86749-8af5-41e5-a334-0e3476dbb32c.png)

## Project Tasks

### Mandatory Tasks

#### :white_check_mark: 0. README, AUTHORS

* Write a README.md:
    * description of the project
    * description of the command interpreter:
        * how to start it
        * how to use it
        * examples
* You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference [Docker’s AUTHORS page](https://raw.githubusercontent.com/moby/moby/master/AUTHORS)
* You should use branches and pull requests on GitHub - it will help you as team to organize your work

#### :white_check_mark: 1. Be pycodestyle compliant!
Write beautiful code that passes the pycodestyle checks.

#### :white_check_mark: 2. Unittests
All your files, classes, functions must be tested with unit tests

    guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
    ...................................................................................
    ...................................................................................
    .......................
    ----------------------------------------------------------------------
    Ran 189 tests in 13.135s

    OK
    guillaume@ubuntu:~/AirBnB$
_Note that this is just an example, the number of tests you create can be different from the above example._

**Warning:**

Unit tests must also pass in non-interactive mode:

    guillaume@ubuntu:~/AirBnB$ echo "python3 -m unittest discover tests" | bash
    ...................................................................................
    ...................................................................................
    .......................
    ----------------------------------------------------------------------
    Ran 189 tests in 13.135s

    OK
    guillaume@ubuntu:~/AirBnB$


### Advanced Tasks


---

### Authors
- [Nasir Abdulrasheed](https://github.com/DrOncogene/) | <mypythtesting@gmail.com>
- [Charles S. Homsuk](https://github.com/Charles-Homks/) | <charles01homks@gmail.com>

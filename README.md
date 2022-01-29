# Welcome to the AirBnB clone project!
![image](https://user-images.githubusercontent.com/88429426/151580771-5675fb20-ad52-46cd-bc55-9f9d937cdee9.png)

## Introduction
This is a clone of the [Airbnb](https://airbnb.com) website, from the backend to the frontend.  
The project consist of the following parts:  
1. Bulding the console to create a data model and manage data objects. Also store and persist them to a **JSON** file, essentially constituting a storage engine.  
2. The static frontend using **HTML/CSS** and a web template for the objects.  
3. **MySQL** database to replace the file storage engine and map the data models to tables in the database by using an **ORM**.  
4. Creating a templating web framework by building a flask based python server that serve the static frontend with objects from the database or file storage engine.  
5. Creating a **RESTful** API using flask for manipulating objects from the frontend.  
6. Making the website dynamic by using **JS** and load objects using the REST API. 

## The console
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

## Files and Directories
- repr(models) directory will contain all classes used for the entire
project. A class, called “model” in a OOP project is the representation
of an object/instance and is used during object manipulation.
- repr(tests) directory will contain all
unit tests of all code coverage.
- repr(console.py) file is the entry
point of our command interpreter.
- repr(models/base_model.py) file is the base class of all our models.
It contains common elements:
    - attributes: repr(id, created_at) and repr(updated_at)
    - methods: repr(save()) and repr(to_json())
- repr(models/engine) directory will contain all storage classes
(using the same prototype). For the moment you will have only
one: repr(file_storage.py.)

---

### Authors
- [Nasir Abdulrasheed](https://github.com/DrOncogene/) | <mypythtesting@gmail.com>
- [Charles S. Homsuk](https://github.com/Charles-Homks/) | <charles01homks@gmail.com>

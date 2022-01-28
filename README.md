## The Airbnb clone project
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
##### Usage
user@system$ ./console.py  
Documented commands (type help \<topic\>):  
EOF  help  quit  
(hbnb)   
(hbnb)   
(hbnb) quit  

$  


### Authors
- [Nasir Abdulrasheed](https://github.com/DrOncogene/) | <mypythtesting@gmail.com>
- [Charles S. Homsuk](https://github.com/Charles-Homks/) | <charles01homks@gmail.com>

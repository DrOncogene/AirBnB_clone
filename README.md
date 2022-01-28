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

    Usage: `monty file`
        where `file` is the path to the file containing Monty byte code
    If the user does not give any file or more than one argument to your program, print the error message `USAGE: monty file`, followed by a new line, and exit with the status `EXIT_FAILURE`
    If, for any reason, it’s not possible to open the file, print the error message `Error: Can't open file <file>`, followed by a new line, and exit with the status `EXIT_FAILURE`
        where `<file>` is the name of the file
    If the file contains an invalid instruction, print the error message `L<line_number>: unknown instruction <opcode>`, followed by a new line, and exit with the status `EXIT_FAILURE`
        where `<line_number>` is the line number where the instruction appears.
        Line numbers always start at 1
    The monty program runs the bytecodes line by line and stop if either:
        it executed properly every line of the file
        it finds an error in the file
        an error occured
    If you can’t malloc anymore, print the error message `Error: malloc failed`, followed by a new line, and exit with status `EXIT_FAILURE`.
    You have to use `malloc` and `free` and are not allowed to use any other function from `man malloc` (realloc, calloc, …)


$  

### Authors
- [Nasir Abdulrasheed](https://github.com/DrOncogene/) | <mypythtesting@gmail.com>
- [Charles S. Homsuk](https://github.com/Charles-Homks/) | <charles01homks@gmail.com>

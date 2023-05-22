# AirBnB Clone - The Console

![hbnb](https://github.com/Omwamii/AirBnB_clone/assets/100716410/4e4c811b-96d5-4ae8-8422-d8f5db10bd38)

**The purpose of this project is to create an command interpreter that will be used to manipulate data in the AirBnB clone**

## Usage

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

```
$ ./console.py
(hbnb) create User
11e3fda9-14c0-49a6-b389-27d945b4a47c
(hbnb)
(hbnb) User.show(11e3fda9-14c0-49a6-b389-27d945b4a47c)
[User] (11e3fda9-14c0-49a6-b389-27d945b4a47c) {'id': '11e3fda9-14c0-49a6-b389-27d945b4a47c', 'created_at': datetime.datetime(2023, 5, 16, 20, 41, 0, 353236), 'updated_at': datetime.datetime(2023, 5, 16, 20, 41, 0, 353236)}
(hbnb)
(hbnb) User.all()
["[User] (c3fd8e85-8131-458d-bd78-7bc478cd0d03) {'id': 'c3fd8e85-8131-458d-bd78-7bc478cd0d03', 'created_at': datetime.datetime(2023, 5, 16, 0, 6, 2, 29797), 'updated_at': datetime.datetime(2023, 5, 16, 0, 6, 2, 29797), 'first_name': 'John', 'age': 89}", "[User] (11e3fda9-14c0-49a6-b389-27d945b4a47c) {'id': '11e3fda9-14c0-49a6-b389-27d945b4a47c', 'created_at': datetime.datetime(2023, 5, 16, 20, 41, 0, 353236), 'updated_at': datetime.datetime(2023, 5, 16, 20, 41, 0, 353236)}"]
(hbnb)
(hbnb) User.destroy(11e3fda9-14c0-49a6-b389-27d945b4a47c)
(hbnb)
(hbnb) User.show(11e3fda9-14c0-49a6-b389-27d945b4a47c)
** no instance found **
(hbnb)
(hbnb) User.all()
["[User] (c3fd8e85-8131-458d-bd78-7bc478cd0d03) {'id': 'c3fd8e85-8131-458d-bd78-7bc478cd0d03', 'created_at': datetime.datetime(2023, 5, 16, 0, 6, 2, 29797), 'updated_at': datetime.datetime(2023, 5, 16, 0, 6, 2, 29797), 'first_name': 'John', 'age': 89}"]
(hbnb)
(hbnb) User.update("c3fd8e85-8131-458d-bd78-7bc478cd0d03", {'first_name': 'YURI', "age": 27}) 
(hbnb)
(hbnb) User.show(c3fd8e85-8131-458d-bd78-7bc478cd0d03)
[User] (c3fd8e85-8131-458d-bd78-7bc478cd0d03) {'id': 'c3fd8e85-8131-458d-bd78-7bc478cd0d03', 'created_at': datetime.datetime(2023, 5, 16, 0, 6, 2, 29797), 'updated_at': datetime.datetime(2023, 5, 16, 0, 6, 2, 29797), 'first_name': 'YURI', 'age': 27}
(hbnb) 
(hbnb) User.count()
1
(hbnb) sdsd.count()
0
(hbnb) quit
$
```

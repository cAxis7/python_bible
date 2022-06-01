import sqlite3

#Connecting to SQLite
conn = sqlite3.connect('mydata.db')
c = conn.cursor()

###Create Tables
#c.execute("""
#    CREATE TABLE persons(
#        first_name TEXT,
#        last_name TEXT,
#        age INTEGER
#    )
#""")
#conn.commit()
#
##Inserting Values
#
#c.execute("""
#    INSERT INTO persons VALUES
#    ('John', 'Smith', 25),
#    ('Anna', 'Smith', 30),
#    ('Mike', 'Johnsun', 40)
#""")
#conn.commit()

#Selecting Values
c.execute("""SELECT * FROM persons
           WHERE last_name = 'Smith'""")
#print(c.fetchall())

# Classes and Tables
class Person():
    def __init__(self, first=None, last=None, age=None) -> None:
        self.first = first
        self.last = last
        self.age = age
    
    def clone_person(self, result) -> None:
        self.first = result[0]
        self.last = result[1]
        self.age = result[2]

# From Table to Object
person1 = Person()
person1.clone_person(c.fetchone())

print(person1.first)
print(person1.last)
print(person1.age)

## From Object to Table
#person2 = Person('Bob', 'Davis', 23)
#
#c.execute("""INSERT INTO persons VALUES
#           ('{}', '{}', '{}')"""
#           .format( person2.first,
#                    person2.last,
#                    person2.age))
#conn.commit()

# Prepared Statements
person = Person("Julia", "Johnsun", 28)

c.execute("INSERT INTO persons VALUES (?, ?, ?)",
(person.first, person.last, person.age))

conn.commit()

c.execute("SELECT * FROM persons")
print(c.fetchall())

conn.close()
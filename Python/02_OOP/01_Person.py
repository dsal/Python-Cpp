class Person:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        print('Name is %s' %self.name)
    def get_age(self):
        print('Age is %s' %self.age)
    def get_info(self):
        print ('Name is %s and age is %i' %(self.name, self.age))
    def birthday(self):
        self.age + self.age + 1
        print ('Happy Birthday %s' %self.name)
    def return_count(self):
        return (Person.count)

Dan = Person('Dan', 40)
Dan.get_name()
Dan.get_info()
Dan.birthday()
Dan.get_age()

Danny = Person('Danny', 12)
Danny.get_info()



"""
A simple data model for a person with a name and age.
count = 0 is a class attribute (shared across all instances).
In the current code it iss never updated, so it always stays 0.

Class Attributes
----------------
count : int
    Number of Person instances created.
    __init__(self, name, age) runs at construction time,
    and stores instance attributes name and age on each object.

Instance Attributes
-------------------
name : str
    Person's name (non-empty).
age : int
    Person's age in years (>= 0).
get_name, get_age, get_info print formatted information about the instance.
"""
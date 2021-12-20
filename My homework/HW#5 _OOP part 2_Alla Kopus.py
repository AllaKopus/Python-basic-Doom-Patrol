# 1
class Laptop:

    def __init__(self):
        battery1 = Battery('This is battery for Dell')
        battery2 = Battery('This is battery for Aser')
        self.battery = [battery1, battery2]

class Battery:

    def __init__(self, voltage):
        self.voltage = voltage

laptop = Laptop()
print(laptop.battery[0].voltage)
print(laptop.battery[1].voltage)
# This is battery for Dell
# This is battery for Aser

# 2
class Guitar:

    def __init__(self, guitarstring):
        self.guitarstring = guitarstring

class GuitarString:

    def __init__(self):
        pass

guitarString = GuitarString()
guitar = Guitar(guitarString)

# 3
class Calc:
    @staticmethod
    def add_nums(a, b, c):
        return a+b+c

sum_add_nums = Calc.add_nums(1, 5, 8)
print(sum_add_nums)
# 14

# 4
class Pasta:

    def __init__(self, ingredients):
        self.ingredient = ingredients

    def __repr__(self):
        return f'Pasta {self.ingredient}'

    @classmethod
    def carbonara(cls):
        return cls(["tomato", "cucumber"])

    @classmethod
    def bolognaise(cls):
        return cls (['bacon', 'parmesan', 'eggs'])

pasta1 = Pasta.carbonara
pasta2 = Pasta.bolognaise
print(pasta1)
print(pasta2)

# 5


# 6
import dataclasses

@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int

# 7
from collections import namedtuple

addressBookDataClass = namedtuple('AddressBookDataClass', ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])
AddressBookDataClass_1 = addressBookDataClass(10, 'Alla', 8648477, 'Mykolaiv', 'abc@ukr.net', '15/10/1987', 35)
print(AddressBookDataClass_1)
# AddressBookDataClass(key=10, name='Alla', phone_number=8648477, address='Mykolaiv', email='abc@ukr.net', birthday='15/10/1987', age=35)

# 8
class AddressBook:

    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = int (key)
        self.name = str (name)
        self.phone_number = str (phone_number)
        self.address = str (address)
        self.email = str (email)
        self.birthday = str (birthday)
        self.age = int (age)

    def __str__(self):
        return f'AddressBook {self.key}, {self.name}, {self.phone_number}, {self.address}, {self.email}, {self.birthday}, {self.age}'

AddressBookDataClass_2 = AddressBook(10, 'Alla', 8648477, 'Mykolaiv', 'abc@ukr.net', '15/10/1987', 35)
print(AddressBookDataClass_2)
# AddressBook 10, Alla, 8648477, Mykolaiv, abc@ukr.net, 15/10/1987, 35

# 9
class Person:
    name = "John"
    age = 36
    country = "USA"

p = Person()
print(p.age)
# 36
setattr(p,'age',30)
print(p.age)
# 30
print(p.name, p.age, p.country)
# John 30 USA

# 10
class Student:

    def __init__(self, id, name):
        self.id = id
        self.name = name

student = Student(17, 'Alla')
setattr(student, 'student_email', 'abc@ukr.net')
print(getattr(student, 'student_email'))
# abc@ukr.net

# 11
class Celsius:

    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature * 1.8 + 32

obj = Celsius(25)
print(obj.temperature)
# 77.0

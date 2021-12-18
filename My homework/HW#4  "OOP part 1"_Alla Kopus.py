# 1
class Car:
    car_type = 'regular car'

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

My_car = Car(max_speed=220, mileage=100)
print(My_car)
# <__main__.Car object at 0x7f71adce1040>

# 2
class Bus(Car):

    def __init__(self, max_speed, mileage, capacity):
        super().__init__(max_speed, mileage)
        self.capacity = capacity

    def seating_capacity(self):
        self.seating_capacity = capacity

School_Bus = Bus(220, 100, 50)
print(School_Bus)
# <__main__.Bus object at 0x7ff5f7ac9250>

# 3
print(type(Bus))

# 4
print(isinstance(Bus, Car))

# 5
class School:

    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_student = number_of_students

My_School = School(15, 345)
print(My_School)
# <__main__.School object at 0x7fd437e173a0>

# 6
class SchoolBus(School, Bus):

    def __init__(self, get_school_id, number_of_students, max_speed, mileage, capacity, bus_school_color):
        School.__init__(self, get_school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, capacity)
        self.bus_school_color = any

    def bus_school_color(self):
        print(f'The SchoolBus is {self.bus_school_color()}.')

My_SchoolBus = SchoolBus(5, 300, 200, 100, 45, 'color')
print(My_SchoolBus)
# <__main__.SchoolBus object at 0x7f4fa0bc6370>

# 7
class Bear:

    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        return (f'Bear make sound like {self.sound}')

class Wolf:

    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        return (f'Wolf make sound like {self.sound}')

My_Bear = Bear('Rrrrr')
My_Wolf = Wolf('Auuuu')
Wild_animals = (My_Bear, My_Wolf)

for animals_sound in Wild_animals:
    print(animals_sound.make_sound())

# Bear make sound like Rrrrr
# Wolf make sound like Auuuu

# 8

class City():

    def __init__(self, name, population_instance_attributes):
        self.name = name
        self.population_instance_attributes = population_instance_attributes

    def __call__(self):
        if  self.population_instance_attributes >= 1500:
            return self.name
        else:
            return (f'Your city is too small')

My_City = City('Turin', 1400)
print(My_City.__call__())

# Your city is too small



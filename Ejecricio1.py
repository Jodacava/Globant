from datetime import datetime


class Person:
    count = 0
    def __init__(self, name, lastname, age, address):
        self.__name = name
        self.__lastname = lastname
        self.age = age
        self.address = address
        Person.count += 1

    def fullName(self):
        return self.__name + " " + self.__lastname

    def noAge(self):
        noageperson = Person(self.__name, self.__lastname, self.age, self.address)
        delattr(noageperson, 'age')
        return noageperson

    @staticmethod
    def countinstances():
        return 'number of instances: ' + str(Person.count)

class Employee(Person):
    def __init__(self, code, name, lastname, age, address, salaryph, startd, position, department):
        Person.__init__(self, name, lastname, age, address)
        self.code = code
        self.salaryph = salaryph
        self.stard = startd
        self.position = position
        self.departement = department

    def dataemployee(self):
        return str(self.code) + " " + self.fullName() + " " + str(self.salaryph)


person1 = Person("Johann", "Castro", 40, "calle 123 # 2 - 30")
person2 = Person("David", "Valencia", 32, "calle 23 # 234 - 20")
person3 = Person("Andrea", "Bernal", 30, "carrer 123 # 50 - 35")
person4 = Person("Natalia", "Nuñez", 25, "calle 140 # 2 - 20")

empl1 = Employee(1, "Johann", "Castro", 40, "calle 123 # 2 - 30", 100, datetime(2020, 8, 1, 0, 0), "Python Developer", "TI")

print(person1.fullName())
print(vars(person1.noAge()))
print(str(Person.countinstances()))
print(empl1.dataemployee())

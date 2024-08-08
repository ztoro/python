from datetime import datetime


class Person:
    def __init__(self, name, age):
        self.height = None
        self.name = name
        self.__age = age
        self.__created_time = self.__get_time()

    def print(self):
        print(self.name)
        print(self.__age)
        print(self.height)
        print(self.__created_time)

    @staticmethod
    def create_person(name, age):
        return Person(name, age)

    def set_height(self, height):
        self.height = height

    def get_age(self):
        return self.__age

    # get-er függvény a private változó eléréséhez
    def get_created_time(self):
        return self.__created_time

    @staticmethod
    def __get_time():
        return datetime.now()



# Származtatott osztály
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def print(self):
        print(self.name)
        # Pythonban a származtatott osztály nem látja a származott osztály private változóit! get-ert hívunk!
        print(self.get_age())
        print(self.height)
        print(self.get_created_time())
        print(self.__salary)


def main():
    person = Person("Tibi", 30)
    person.print()
    person.set_height(180)
    print(person.get_age())
    print(person.height)
    employee = Employee("Gabor", 29, 500)
    employee.print()
    person = Person.create_person("Peter", 30)
    person.print()
    employee = create_employee()
    employee.print()


def create_employee():
    name = "Zoli"
    age = 5*6
    height = 180
    employee = Employee(name, age, 500)
    employee.set_height(height)
    return employee


if __name__ == '__main__':
    main()

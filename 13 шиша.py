class Employee:
    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age
    def show_info(self):
        print(f"Имя: {self.__name}")
        print(f"Зарплата: {self.__salary}")
        print(f"Возраст: {self.__age}")
emp = Employee("temka", 70000, 29)
emp.show_info()
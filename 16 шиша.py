class Employee:
    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age
    def get_name(self):
        return self.__name
    def get_salary(self):
        return self.__salary
    def get_age(self):
        return self.__age
emp = Employee("thxrel", 70000, 29)
print(emp.get_name())
print(emp.get_salary())
print(emp.get_age())
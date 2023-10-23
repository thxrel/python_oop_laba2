class User:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


class Employee(User):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

    def setLastName(self, last_name):
        self.last_name = last_name

    def getLastName(self):
        return self.last_name

employee = Employee("Temka", 15000)

employee.setName("Liza")
print(employee.getName())


employee.setSalary(6000)
print(employee.getSalary())

employee.setLastName("tHxrel")
print(employee.getLastName())
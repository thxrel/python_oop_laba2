class Employee:
    __age = None
    __salary = None

    def getAge(self):
        return self.__age

    def getSalary(self):
        return str(self.__salary) + "$"

    def setAge(self, age):
        if 0 <= age <= 120:
            self.__age = age
        else:
            raise Exception("age is incorrect!")

    def setSalary(self, salary):
        self.__salary = salary

employee = Employee()
employee.setAge(29)
print(employee.getAge())

employee.setSalary(7000)
print(employee.getSalary())
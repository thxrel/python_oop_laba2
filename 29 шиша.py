class User:
  def setName(self, name):
    self.name = name

  def getName(self):
    return self.name

class Employee(User):
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

employee = Employee("Temka", 15000)

employee.setName("Liza")
print(employee.getName())
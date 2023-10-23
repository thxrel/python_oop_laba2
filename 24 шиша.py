class Employee:
  name = None
  salary = None

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

employees = [
   Employee('Temka', 15000),
   Employee('Liza', 9000),
   Employee('vanya', 4000),
]

for employee in employees:
  print("Name:", employee.name)
  print("Salary:", employee.salary)
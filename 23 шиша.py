class Position:
  position = None

  def __init__(self, position):
    self.position = position

class Department:
  department = None

  def __init__(self, department):
    self.department = department

class User:
  name = None
  position = None
  department = None

  def __init__(self, name, position, department):
    self.name = name
    self.position = position
    self.department = department

position = Position("yborshik")
department = Department("mira")
user = User("temka", position, department)

print(user.name)
print(user.position.position)
print(user.department.department)
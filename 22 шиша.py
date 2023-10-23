class Validator:
  def isEmail(self, string):
    pass
  def isDomain(self, string):
   pass

  def isNumber(self, string):
    pass


class Validator:
  def isEmail(self, string):
    if "@" in string and "." in string:
      return True
    else:
      return False


validator = Validator()
print(validator.isEmail("example@mail.com"))  # True
print(validator.isEmail("example.com"))  # False
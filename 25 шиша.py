class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class EmployeesCollection:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        for employee in self.employees:
            print(employee.name)

    def total_salary(self):
        total = 0
        for employee in self.employees:
            total += employee.salary
        return total

    def average_salary(self):
        if len(self.employees) == 0:
            return 0
        total_salary = self.total_salary()
        average = total_salary / len(self.employees)
        return average


employees_collection = EmployeesCollection()

employee1 = Employee("Temka", 15000)
employee2 = Employee("Liza", 9000)
employee3 = Employee("Vanya", 4000)

employees_collection.add_employee(employee1)
employees_collection.add_employee(employee2)
employees_collection.add_employee(employee3)

employees_collection.show_employees()
total_salary = employees_collection.total_salary()
average_salary = employees_collection.average_salary()

print("Total Salary:", total_salary)
print("Average Salary:", average_salary)
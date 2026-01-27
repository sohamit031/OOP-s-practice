from abc import ABC, abstractmethod

class Employee(ABC):
    
    def __init__(self, name):
        self.name = name

    # The Contract: "Every employee MUST have a calculate_salary method"
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTime(Employee):
    def calculate_salary(self):
        return 5000  # Fixed salary for full-timers

class Intern(Employee):
    def calculate_salary(self):
        hours_worked = 100
        hourly_rate = 10
        return hours_worked * hourly_rate  # Interns get paid by the hour

# 1. Create the employees
alice = FullTime("Alice")
bob = Intern("Bob")

# 2. Put them in a list
company_staff = [alice, bob]

# 3. Pay them
for staff in company_staff:
    print(f"{staff.name} earned ${staff.calculate_salary()}")
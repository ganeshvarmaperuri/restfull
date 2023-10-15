"""
In class we three different types of methods
1. Regular Method(Instance Method i.e it takes self as an argument)
2. Class Method (It can call constructor to itself)
3. Static Method
"""

import datetime


class Employee:
    min_hike = 1.5

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def get_fullname(self):
        return f"{self.first} {self.last}"

    def get_hike(self):
        return int(self.salary * Employee.min_hike)

    @classmethod
    def change_hike(cls, value):
        cls.min_hike = value

    @classmethod
    def get_emp_details(cls, text):
        first, last, salary = text.split(",")
        return cls(first, last, int(salary))

    @staticmethod
    def is_weekday(date):
        if date.weekday() in (5, 6):
            return False
        return True


emp1 = Employee("first1", "last1", 5000)
print(emp1.get_hike())  # output: 7500
Employee.min_hike = 2
print(emp1.get_hike())  # output: 10000

"""
Instead of giving new values like ---> Employee.min_hike = 2

we can write a class method to change the values of the attributes
"""

Employee.change_hike(3)
print(emp1.get_hike())  # output: 15000

list_of_employees_details = [
    "raju,p,5541",
    "santosh,y,8451",
    "ravi,s,8000",
    "ganesh,p,10000",
    "sai,k,6000",
    "Rahul,p,5000",
    "srinu,l,8000",
]

emp2 = Employee.get_emp_details(list_of_employees_details[0])
print(emp2.first)  # output: raju
print(emp2.get_hike())  # output: 16623

my_date = datetime.date(2016, 5, 1)
print(emp2.is_weekday(datetime.datetime.today().date()))  # output: True

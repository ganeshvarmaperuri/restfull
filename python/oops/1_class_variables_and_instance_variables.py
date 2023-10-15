class Employee:
    """
    min_hike = 1.05 <--- this class variable

    the value of this variable is same for every objects,
    if we want to change the value of the class variable for any particular object we need to assign a new
    value to the class variable to that particular object
    """

    min_hike = 1.05
    no_of_objects_on_this_class = 0

    def __init__(self, first, last, salary):
        """
        variables we are defining in the __init__ method are instance variables
        the values for this variables are different for every instance of this class
        """
        self.first = first
        self.last = last
        self.salary = salary

        Employee.no_of_objects_on_this_class += 1

    def emp_salary(self):
        return self.salary

    def email(self):
        return f"{self.first}{self.last}@company.com"

    def emp_fullname(self):
        return f"{self.first} {self.last}"

    def hike(self):
        """
        the class variables can also be accessed as a instance variables,

        how it happens means, whenever we call a variable, first it will check in instance variables, if it is not
        available in there then it check in class variables

        int(self.salary * Employee.min_hike) accessing as a class variable
        if we call the variable with class name, you can't change the value at instance level


        int(self.salary * self.min_hike) accessing as a instance variable
        if we call the variable with instance, you can change the value at instance level



        here min_hike is same value for all the instances
        :return:
        """
        # return int(self.salary * Employee.min_hike)
        return int(self.salary * self.min_hike)

    def hike_with_class_variable(self):
        return int(self.salary * Employee.min_hike)

    def hike_with_instance_variable(self):
        return int(self.salary * self.min_hike)


emp1 = Employee("first1", "last1", 1000)
emp2 = Employee("first2", "last2", 2000)

print(emp1.hike())  # output: 1050
print(emp2.hike())  # output: 2100

print(Employee.min_hike)  # output: 1.05

Employee.min_hike = 2.5  # changing the class variable value

print(emp1.hike())  # output: 2500
print(emp2.hike())  # output: 5000

emp1.min_hike = 3  # changing the class variable value on this particular object

print(emp1.hike_with_class_variable())  # output: 2500
print(emp1.hike_with_instance_variable())  # output: 3000

print(Employee.no_of_objects_on_this_class)  # output: 2

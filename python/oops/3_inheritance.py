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


class Developer(Employee):
    min_hike = 2

    def __init__(self, first, last, salary, programing_lang):
        super().__init__(first, last, salary)
        self.programing_lang = programing_lang

    def get_hike(self):
        return int(self.salary * Developer.min_hike)


class Manager(Employee):
    def __init__(self, first, last, salary, team=None):
        super().__init__(first, last, salary)
        if self.team is None:
            self.team = []
        else:
            self.team = team

    def add_dev(self, dev):
        if dev not in self.team:
            self.team.append(dev)
        else:
            print(f"{dev} is already in your team")

    def remove_dev(self, dev):
        if dev in self.team:
            self.team.remove()
        else:
            print(f"{dev} is not in your team")

    def get_team_size(self):
        return len(self.team)


dev1 = Developer("first1", "last1", 5000, "python")
print(dev1.get_hike())

mng1 = Manager("mngfirst1", "mnglast1", 5000, None)
print(dev1.get_fullname())

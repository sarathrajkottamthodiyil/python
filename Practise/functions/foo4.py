class employee:
    empcount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        employee.empcount += 1
    def displayemployee(self):
        print("name :", self.name, "salary:", self.salary)
emp1 = employee("arun", 5000)
emp2 = employee("aki", 10000)
emp1.displayemployee()
emp2.displayemployee()
print("total employee %d" % employee.empcount)
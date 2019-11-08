class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def details(self):
        print("employee name:",  self.name)
        print("employee age", self.age)
emp = employee("sam", 36)
emp.details()
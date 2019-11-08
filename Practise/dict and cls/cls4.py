class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("hello my name is" + self.name)
p1 = person("john", 36)
p1.age = 40
p1.name = "jack"
print(p1.age)
print(p1.name)

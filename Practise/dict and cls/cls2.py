class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("hello my name is" ' ' + self.name)
        print("hello my age is" ' ' + str(self.age))

p1 = person("john", 36)
p1.myfunc()
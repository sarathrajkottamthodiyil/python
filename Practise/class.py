class myclass:
    variable = "foo"
    def function(self):
        print("this is a message inside the class>.")
myobjectx = myclass()
print(myobjectx.variable)

print("***************************")
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

car3 = Vehicle()
car3.name = "breza"
car3.color = "gold"
car3.kind = "xuv"
car3.value = 12000.00


print(car1.description())
print(car2.description())
print(car3.description())

print("***************************************")

class human:
    name = ""
    age = 100
    speak = ""
    job = ""

    def details(self):
        det_str = "%s is %d year old he can speak %s and his job is %s" % (self.name, self.age, self.speak, self.job)
        return  det_str
hum1 = human()
hum1.name = "sarath"
hum1.age =  23
hum1.speak = "english"
hum1.job = "developer"

hum2 = human()
hum2.name = "arun"
hum2.age =  24
hum2.speak = "hindi"
hum2.job = "teacher"

print(hum1.details())
print(hum2.details())

class myclass:
    "this is my second class"
    a = 10
    def func(self):
        print('hello')

ob = myclass()

print(myclass.a)

print(ob.func())

print(myclass.__doc__)

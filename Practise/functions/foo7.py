def create_adder(x):
    def adder(y):
        return x+y
    return adder

add = create_adder(20)
print (add(15))
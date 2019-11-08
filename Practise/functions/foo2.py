def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(8))
print("**********************")
def my_function(child3, child2, child1):
    print("the youngest child is" ' '  + child3)
my_function(child3= "sriya", child2= "kannan", child1= "minnu")
print("************************")

def my_function(*kids):
    print("the youngest child is " ' ' + kids[2])
my_function("jack", "jain", "jin")

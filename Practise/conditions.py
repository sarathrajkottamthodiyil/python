x = 2
print(x == 2)
print(x == 3)
print(x < 3)

#####boolean operators#########

name = "john"
age = 23
if name == "john" and age == 23:
    print("your name is  john, and you are also 23 years old.")
if name == "john" or name == "rick":
    print("your name is either john or rick")

######in operator#######

name = "john"
if name in ["john", "rick"]:
    print("your name is either john or rick")

    ##################

x = 2
if x ==2:
    print("x equals two")
else:
    print("x does not equal to two")

    #############


number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]
print("****************")

if number > 15 :
    print("1")
if first_array:
    print("2")
if len(second_array) == 2:
    print("3")
if len(first_array) + len(second_array) == 5:
    print("4")
if first_array and  first_array[0] == 1:
    print("5")
if not second_number:
    print("6")

print("****************************")
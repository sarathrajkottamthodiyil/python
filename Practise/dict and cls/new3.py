x = int(input("enter the number you want:"))
avg = []
a = 0

def race(foo):
    global a
    print("length is " + str(len(foo)))
    total = 0
    for n in foo:
        total = total + n
    print(total)
    j = total / len(foo)
    a = j
    return j

def note():
    output = a
    file = open("total.txt", "w")
    file.write(str(output))
    file.close()

if x > 0:
    for i in range(x):
       num = i + 1
       y = int(input("enter the %s number:" %num))
       avg.append(y)
       print(avg)

    print("%%%%%%%%%%%%%%%%%%%%%")
    print("avg of given numbers is :", race(avg))
    print("%%%%%%%%%%%%%%%%%%%%%")

    note()
else:
    print("please enter a valid number")
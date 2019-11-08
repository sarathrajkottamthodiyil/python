def foo(first, second, third, *therest):
    print("first: %s" %(first))
    print("second: %s" %(second))
    print("third: %s" %(third))
    print("and all the rest numbers are... %s" %(list(therest)))
foo(1,2,3,4,5,6,7,8,9)

print("***********************************")

def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))
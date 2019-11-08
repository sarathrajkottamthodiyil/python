def shout(text):
    return text.upper()
def loud(text):
    return text.lower()
def greet(func):
    greeting = func("hi, i am created by a function passed as an argument")
    print (greeting)

greet(shout)
greet(loud)
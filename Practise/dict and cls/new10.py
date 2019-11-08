from random import randint
from clear_screen import clear
import time
count = 0
c = []
guess = []
temp_names = []
print("!!! ITS TIME TO CHECK YOUR MEMORY POWER !!!")
f = open("animals.txt", "r")
for i in f:
    d = i.strip()
    temp_names.append(d)
for i in range(5):
    random_index = randint(0, len(temp_names))
    c.append(temp_names[random_index])
print(str(c), end="", flush=True)

time.sleep(2)
print("\b"*100)
# print(" "*100)
for i in range(5):
    guess.append(input("enter the name:"))
for i in range(5):
    if guess[i].casefold() == c[i].casefold():
        count += 1
if count < 1:
    print("!!! YOUR MEMORY IS VERY LOW !!!")
if count == 5:
    print("!!! YOU ARE BRILLIANT !!!")
print("you are corrected:", count)
print("given names:", c)
print("your answers:", guess)
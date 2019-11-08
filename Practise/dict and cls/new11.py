from threading import *
import time
class Demo:
    def num(self):
        for i in range(1, 6):
            print("the number is", i)
            time.sleep(1)
    def double(self):
        for i in range(1, 6):
            print("the double of the number is", 2*i)
            time.sleep(1)

    def square(self):
        for i in range(1, 6):
            print("the square of the number is", i*i)
            time.sleep(1)


a = Demo()
t1 = Thread(target=a.num)
t2 = Thread(target=a.double)
t3 = Thread(target=a.square)

t1.start()
time.sleep(0.2)
t2.start()
time.sleep(0.2)
t3.start()

t1.join()
t2.join()
t3.join()
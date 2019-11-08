class myclass():
    def method1(self):
        print("welcome")

    def method2(self, anything):
        print("how are you :: " + anything)

def main():
    c = myclass()
    c.method1()
    c.method2("i am fine wt abt u")
if __name__== "__main__":
    main()


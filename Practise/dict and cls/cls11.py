class Family:
     def show_family(self):
        print("this is my family")

class Father(Family):
     fathername = ""
     def show_father(self):
        print(self.fathername)

class Mother(Family):
    mothername = ""

    def show_mother(self):
        print(self.mothername)

class Sister(Family):
    sistername = ""
    def show_sister(self):
        print(self.sistername)

class My(Family):
    myname = ""
    def my_name(self):
        print(self.myname)

class Son(Father, Mother, Sister, My):
    def show_parent(self):


        print("myname:", self.myname)
        print("Father:", self.fathername)
        print("Mother:", self.mothername)
        print("Sister:", self.sistername)
S1 = Son()
S1.myname = "george"
S1.fathername = "mark"
S1.mothername = "sonia"
S1.sistername = "jesica"

S1.show_family()
S1.show_parent()
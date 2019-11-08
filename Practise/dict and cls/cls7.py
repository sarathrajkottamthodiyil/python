class Rocket:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
    def launch(self):
        return "%s has reached %s" % (self.name, self.distance)
class marsrover(Rocket):
    def __init__(self, name, distance, maker):
        Rocket.__init__(self, name, distance)
        self.maker = maker

    def get_maker(self):
        return "%s launched by  %s " % (self.name, self.maker)
class MarsRoverComp():
    def __init__(self, name, distance, maker):
        self.rocket = Rocket(name, distance)

        self.maker = maker

    def get_maker(self):
        return "%s Launched by %s" % (self.rocket.name, self.maker)

if  __name__  ==  "__main__":
    x = Rocket("simple rocket", "till stratosphere")
    y = marsrover("VIKRAM_LANDER", "till MOON", "ISRO")
    z = marsrover("mars_rover2", "till Mars", "ISRO")
    print(x.launch())
    print(y.launch())
    print(y.get_maker())
    print(z.launch())
    print(z.get_maker())


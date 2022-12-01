class person():
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.nationality = args[2]

    def myfunc(self):
        print("Hello my name is {} and age is {}. I'm an {}.".format(self.name, self.age, self.nationality))


P1 = person("John", 40, "American")
P1.myfunc()
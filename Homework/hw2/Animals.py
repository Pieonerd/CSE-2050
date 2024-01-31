class Animal:
    def __init__(self, name):
        self.name = name

    def reply(self):
        return self.speak()


class Mammal(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)


class Cat(Mammal):
    def __init__(self, name):
        Mammal.__init__(self, name)
    
    def speak(self):
        return f'{self.name} says Meow!'


class Dog(Mammal):
    def __init__(self, name):
        Mammal.__init__(self, name)

    def speak(self):
        return f'{self.name} says Bark!'


class Primate(Mammal):
    def __init__(self, name):
        Mammal.__init__(self, name)

    def speak(self):
        return f'{self.name} says Hello!'


class ComputerScientist(Primate):
    def __init__(self, name):
        Primate.__init__(self, name)
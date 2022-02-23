class Pet:
    def nickname(self, name):
        self.name = name
        return print(self.name)

class Cat(Pet):
    def voice(self):
        print("Meow")

class Dog(Pet):
    def voice(self):
        print("Woof")

one = Pet()
two = Cat()
three = Dog()
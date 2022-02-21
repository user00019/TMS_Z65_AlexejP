#11.01
class Dog:
    pass
#11.02
class Dog1:
    x = 5
    y = "Woof"
dog100 = Dog1()
dog200 = Dog1()
print(dog100.x)
print(dog200.y)
#11.03
class Dog2:
    def run(self):
        print("run!")
    def jump(self):
        print("jump!")
dog2 = Dog2()
dog2.run()
dog2.jump()
#11.04
class Dog3:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
    def run(self):
        print("run")
    def jump(self):
        print("jump")
    def bark(self):
        print("bark")
dog3 = Dog3(50, 20, "Woofie", 5)
print(f"Рост: {dog3.height}, вес: {dog3.weight}, кличка: {dog3.name}, возраст: {dog3.age}")
dog3.bark(), dog3.jump(), dog3.run()

#11.05
class Dog4:
    def __init__(self, name):
        self.name = name
    def change_name(self, name):
        self.name = name
x = Dog4(name="Goofie")
print(x.__dict__)
print(x.name)
x.change_name("Woofie")
print(x.__dict__)
print(x.name)

#11.06(???)
class Dog5:
    def __init__(self, master):
        self.__master = master
    def get_master(self):
        return print(dog11._Dog5__master)
dog11 = Dog5("boss")
dog11.get_master()

#11.07
class Person:
    def __init__(self, address="Minsk"):
        self.__address = address
    def get_address(self):
        return self.__address
    def set_address(self, address):
        self.__address = address
p1 = Person()
print(p1.get_address())
p1.set_address("Tokyo")

#11.09
class Dog:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master
    def run(self):
        print("I can run")
    def jump(self):
        print("I can jump")
    def birthday(self):
        return self.age + 1
    def sleep(self):
        print("I like to sleep")
    def bark(self):
        print("I can bark")

class Cat:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master
    def run(self):
        print("I can run")
    def jump(self):
        print("I can jump")
    def birthday(self):
        return self.age + 1
    def sleep(self):
        print("I like to sleep")
    def meow(self):
        print("I can meow")

class Parrot:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master
    def run(self):
        print("I can run")
    def jump(self):
        print("I can jump")
    def birthday(self):
        return self.age + 1
    def sleep(self):
        print("I like to sleep")
    def fly(self):
        print("I can fly")

dog144 = Dog("Hachiko", 2, "Richard")
cat1 = Cat("Tom", 5, "Jerry")
parrot1 = Parrot("Captain Flint", 12, "John Silver")

#11.10
class Pet:
    def run(self):
        print("I can run")
    def jump(self):
        print("I can jump")
    def sleep(self):
        print("I like to sleep")

class Dog(Pet):
    def bark(self):
        print("I can bark")

class Cat(Pet):
    def meow(self):
        print("I meow")

class Parrot(Pet):
    def fly(self):
        print("I can fly")
dog10 = Dog()
cat10 = Cat()
parrot10 = Parrot()
cat10.sleep(), cat10.meow(), cat10.run(), cat10.jump()




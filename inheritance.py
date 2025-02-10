class animal:
    def speak(self):
        print("Animal is speaking")

        #child class/sub class/ derived class

class dog(animal):
    def bark(self):
        print("Dog is barking")

class cat(dog):
    def meow(self):
        print("Cat is meowing")

a=animal()


d=dog()
d.speak()

c=cat()





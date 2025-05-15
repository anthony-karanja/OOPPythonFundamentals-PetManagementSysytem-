class Pet:
    def speak(self):
        print("Sound made")
        return ("pet spoke")
    
Rasmus = Pet()
Rasmus.name = Rasmus
print(Rasmus.name)
print(Rasmus.speak())

class Dog:
    species = "canis lupus familiaris"

    def __init__(self,name,breed,age="N/A"):
        self.name = name
        self.breed = breed
        self.age = age

    def speak(self):
        return f"{self.name} says woof!"
    
koba = Dog("koba, Great Dane", 3)
amad = Dog("Amad, Black goat") #we initialized with a default value
koba.age = 4
print(koba.speak())
print(koba.age)
print(amad.age)
print(amad.species)
print(koba.species)

class Cat:
    pass

class Rat:
    pass
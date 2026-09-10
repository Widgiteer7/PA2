
class Car:
    def __init__(self, speed, time):
        self.speed = speed
        self.time = time

# Class "Car" sets attributes for speed & time

    def distance(self):
        return self.speed * self.time

# Program calculates distance with formula v*t = d

car1 = Car(70, 6)
car2 = Car(70, 10)
car3 = Car(70, 15)

# Numbers for distance formula are given

print(f"In {car1.time} hours, the car will travel {car1.distance()} miles.")
print(f"In {car2.time} hours, the car will travel {car2.distance()} miles.")
print(f"In {car3.time} hours, the car will travel {car3.distance()} miles.")

# Results displayed for each car individually
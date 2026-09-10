
 class Car:
    def __init__(self, speed, time):
        self.speed = speed
        self.time = time

    def distance(self):
        return self.speed * self.time

choice = str(input("Do you want to enter the car/'s speed/? (y//n) "))
if choice == "y":
    car1 = Car(70, int(input("Hours car travels for first: ")))
    car2 = Car(70, int(input("Hours car travels for second: ")))
    car3 = Car(70, int(input("Hours car travels for third: ")))
elif choice == "n":
    car1 = Car(70, 6)
    car2 = Car(70, 10)
    car3 = Car(70, 15)
else:
    print("Enter 'y' or 'n'.")


print(f"In {car1.time} hours, the car will travel {car1.distance()} miles.")
print(f"In {car2.time} hours, the car will travel {car2.distance()} miles.")
print(f"In {car3.time} hours, the car will travel {car3.distance()} miles.")

# program refuses input command despite having worked before
# check if parenthesis in variable is causing error?
# but why would that affect anything above?
# revisit command itself, maybe improper syntax for string input

# also figure out how to make the program loop on choice input command for invalid response
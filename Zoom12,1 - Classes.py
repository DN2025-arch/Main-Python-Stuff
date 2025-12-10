class Student():
    def __init__(self, n, a, l, h):
        self.name = n
        self.age = a
        self.lessons = l
        self.house = h
    def display(self):
        print(f"Student {self.name}")
        print(f"They are {self.age} years old")
        print(f"They come from the {self.house} Tutor Group.")
        print(f"They have {self.lessons} today.")
    def update(self):
        self.name = input("New Name:")
        self.age = int(input("New Age:"))
        self.house = input("New House:")

class Car():
    def __init__(self, m, y, sp, st):
        self.model = m
        self.year = y
        self.speed = sp
        self.seats = st
    def display(self):
        print(f"Car Model: {self.model}")
        print(f"Year of Creation: {self.year}")
        print(f"Max Speed: {self.speed} mph")
        print(f"Seats: {self.seats}")

veronica = Student("Vec", 12, ["Maths", "English", "Spanish"], h="Red")

print(veronica.name)

veronica.display()

car1 = Car("Volkswagen", 2011, 168, 4)

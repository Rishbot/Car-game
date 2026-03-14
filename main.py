class Map:
    def __init__(self, type):
        self.type = type
    def _display_block(self):
        if self.type == "plain":
            print(" ", end=" ")
        elif self.type == "grid":
            print(".", end=" ")

    def display(self, car):
        row = car.x
        column = car.y
        for i in range(25):
            for j in range(25):
                if i == row and j == column:
                    print("X", end=" ")
                else:
                    self._display_block()
            print()

class Car: 
    def __init__(self, brand, fuel, speed, x, y):
        self.brand = brand
        self.fuel = fuel
        self.speed = speed
        self.x = x
        self.y = y
    def forward(self):
        print("The car is moving forward")
        self.y = self.y + self.speed
    def backward(self):
        print("The car is moving backward")
        self.y = self.y - self.speed
    def left(self):
        print("The car is moving left")
        self.x = self.x - self.speed
    def right(self):
        print("The car is moving right")
        self.x = self.x + self.speed
    
car1 = Car("BMW", 100, 1, 0, 0)
map = Map("plain")

while True:
    print("INFORMATION OF CAR1")
    map.display(car1)
    control = input("Enter the control for the car (w, a, s, d): ")
    if control == "w":
        car1.forward()
    elif control == "s":
        car1.backward()
    elif control == "a":
        car1.left()
    elif control == "d":
        car1.right()
    elif control == "p":
        print("Exiting the program")
        break
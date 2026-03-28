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

class Map:
    def __init__(self, type: str, goal:dict = {"x": 0, "y": 0}):
        self.type = type
        self.completed = False
        self.goal = goal
    def _display_block(self):
        if self.type == "plain":
            print(" ", end=" ")
        elif self.type == "grid":
            print(".", end=" ")

    def display(self, cars: list[Car]):
        cars_positions = [{"brand": car.brand, "x": car.x, "y": car.y} for car in cars]
        print(cars_positions)
        for i in range(25):
            for j in range(25):
                car_found = False
                for car in cars_positions:
                    if car["x"] == i and car["y"] == j:
                        print(car['brand'], end=" ")
                        car_found = True
                        break
                if i == self.goal["x"] and j == self.goal["y"] and not car_found:
                    print("O", end=" ")
                else:
                    if not car_found:    
                        self._display_block()
                if cars[0].x == self.goal["x"] and cars[0].y == self.goal["y"]:
                    self.completed = True
            print()
    
car1 = Car("X", 100, 1, 13, 13)
car2 = Car("+", 100, 1, 11, 11)
cars = [car1, car2]
map = Map("grid", {"x": 12, "y": 12})

while True:
    print("INFORMATION OF CAR1")
    map.display(cars)
    if map.completed:
        print("You Win!")
        break
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
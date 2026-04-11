import random

class Car: 
    def __init__(self, brand, size, fuel, speed, x, y):
        self.brand = brand
        self.size = size
        self.fuel = fuel
        self.speed = speed
        self.x = x
        self.y = y
    def forward(self):
        self.y = self.y - self.speed
    def backward(self):
        self.y = self.y + self.speed
    def left(self):
        self.x = self.x - self.speed
    def right(self):
        self.x = self.x + self.speed

class EnemyCar(Car):
    def __init__(self, brand, size, fuel, speed, x, y):
        super().__init__(brand, size, fuel, speed, x, y)
        self.caught_player = False
    def move(self, car: Car):
        if self.x > car.x:
            self.left()
        elif self.x < car.x:
            self.right()
        if self.y > car.y:
            self.forward()
        elif self.y < car.y:
            self.backward()
        if abs(self.x - car.x) < self.size - 10 and abs(self.y - car.y) < self.size - 10:
            print("Game Over!")
            self.caught_player = True
        

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
                    if car["y"] == i and car["x"] == j:
                        print(car['brand'], end=" ")
                        car_found = True
                        break
                if i == self.goal["y"] and j == self.goal["x"] and not car_found:
                    print("O", end=" ")
                else:
                    if not car_found:    
                        self._display_block()
                if abs(cars[0].x - self.goal["x"]) < 50 and abs(cars[0].y - self.goal["y"]) < 50:
                    self.completed = True
            print()

car1 = Car("X", 100, 1, 1, random.randint(0,24), random.randint(0,24))
car2 = EnemyCar("+", 100, 4, 1, random.randint(0,24), random.randint(0,24))
cars = [car1, car2]
map = Map("grid", {"x": 12, "y": 12})

'''
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
    if not car2.caught_player:
        if random.randint(0, 1) == 0:
            car2.move(car1)
    else:
        print("Game Over!")
        exit()

'''
from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, name, wheel_size, wheel_number):
        super().__init__(wheel_size, wheel_number)
        self.name = name

    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

mazda = Car("Mazda", 21, 4)
print(mazda.go())

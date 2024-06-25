# **kwargs return a dictionary


def calculator(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculator(1, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)

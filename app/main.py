class Car:
    def __init__(self, model: str) -> None:
        self.model = model
        self.cleaned = False


class CarWashStation:
    def __init__(self) -> None:
        self.cars_washed = 0

    def wash(self, car: Car) -> None:
        car.cleaned = True
        self.cars_washed += 1

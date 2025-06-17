class Car:
    def __init__(self, model: str):
        self.model = model
        self.cleaned = False


class CarWashStation:
    def wash(self, car: Car) -> None:
        car.cleaned = True

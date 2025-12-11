class Car:
    def __init__(self, model: str, is_clean: bool = False) -> None:
        self.model = model
        self.is_clean = is_clean

    def wash(self) -> None:
        self.is_clean = True


class CarWashStation:
    def __init__(self) -> None:
        self.was_cleaned = 0

    def wash_car(self, car: Car) -> None:
        car.wash()
        self.was_cleaned += 1

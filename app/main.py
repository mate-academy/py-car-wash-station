from typing import Optional

class Car:
    def __init__(self, model: str, color: str, is_dirty: bool = True) -> None:  # ANN204 fixed
        self.model: str = model
        self.color: str = color
        self.is_dirty: bool = is_dirty

    def wash(self) -> None:  # ANN201 fixed
        if self.is_dirty:
            self.is_dirty = False
            print(f"{self.model} has been washed.")
        else:
            print(f"{self.model} is already clean.")

    def __str__(self) -> str:  # ANN204 fixed
        status = "dirty" if self.is_dirty else "clean"
        return f"{self.color} {self.model} ({status})"


class CarWashStation:
    def __init__(self) -> None:  # ANN204 fixed
        self.cars_washed: int = 0

    def wash_car(self, car: Car) -> None:  # ANN201 fixed
        if car.is_dirty:
            car.wash()
            self.cars_washed += 1
        else:
            print(f"{car.model} does not need washing.")

    def __str__(self) -> str:  # ANN204 fixed
        return f"Cars washed so far: {self.cars_washed}"

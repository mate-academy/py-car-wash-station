from typing import List


class Car:
    def __init__(self, license_plate: str, color: str, is_dirty: bool = True) -> None:
        self.license_plate = license_plate
        self.color = color
        self.is_dirty = is_dirty

    def wash(self) -> None:
        self.is_dirty = False

    def __repr__(self) -> str:
        status = "dirty" if self.is_dirty else "clean"
        return f"Car({self.license_plate}, {self.color}, {status})"


class CarWashStation:
    def __init__(self) -> None:
        self.queue: List[Car] = []

    def add_car(self, car: Car) -> None:
        self.queue.append(car)

    def wash_next_car(self) -> None:
        if self.queue:
            car = self.queue.pop(0)
            car.wash()
            print(f"{car.license_plate} has been washed.")
        else:
            print("No cars in the queue.")

    def __repr__(self) -> str:
        return f"CarWashStation({len(self.queue)} cars in queue)"

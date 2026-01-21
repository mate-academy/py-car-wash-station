class Car:
    def __init__(self, model: str, color: str, is_dirty: bool = True) -> None:
        self.model: str = model
        self.color: str = color
        self.is_dirty: bool = is_dirty

    def wash(self) -> None:
        if self.is_dirty:
            self.is_dirty = False
            print(f"{self.model} has been washed.")
        else:
            print(f"{self.model} is already clean.")

    def __str__(self) -> str:
        status = "dirty" if self.is_dirty else "clean"
        return f"{self.color} {self.model} ({status})"


class CarWashStation:
    def __init__(
        self,
        bays: int,
        water_liters: int,
        price_per_wash: float,
        max_capacity: int,
    ) -> None:
        self.bays: int = bays
        self.water_liters: int = water_liters
        self.price_per_wash: float = price_per_wash
        self.max_capacity: int = max_capacity
        self.cars_washed: int = 0

    def wash_car(self, car: Car) -> None:
        if car.is_dirty:
            car.wash()
            self.cars_washed += 1
        else:
            print(f"{car.model} does not need washing.")

    def __str__(self) -> str:
        return f"Cars washed so far: {self.cars_washed}"

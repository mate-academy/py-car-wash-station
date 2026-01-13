class Car:
    def __init__(self, model: str, color: str, is_dirty: bool = True):
        self.model = model
        self.color = color
        self.is_dirty = is_dirty

    def wash(self):
        """Clean the car."""
        if self.is_dirty:
            self.is_dirty = False
            print(f"{self.model} has been washed.")
        else:
            print(f"{self.model} is already clean.")

    def __str__(self):
        status = "dirty" if self.is_dirty else "clean"
        return f"{self.color} {self.model} ({status})"


class CarWashStation:
    def __init__(self):
        self.cars_washed = 0

    def wash_car(self, car: Car):
        """Wash a car and increment counter."""
        if car.is_dirty:
            car.wash()
            self.cars_washed += 1
        else:
            print(f"{car.model} does not need washing.")

    def __str__(self):
        return f"Cars washed so far: {self.cars_washed}"


# Example usage:
car1 = Car("Toyota Corolla", "Red")
car2 = Car("Honda Civic", "Blue", is_dirty=False)

station = CarWashStation()
station.wash_car(car1)  # Should wash
station.wash_car(car2)  # Already clean

print(station)  # Cars washed so far: 1

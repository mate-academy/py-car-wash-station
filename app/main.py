class Car:
    def __init__(self, seats: int, comfort_class: int | str, brand: str) -> None:
        self.seats = seats
        self.comfort_class = str(comfort_class).lower()
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        max_cars: int,
        water_capacity: float,
        soap_capacity: float,
        price_per_class: float
    ) -> None:
        self.max_cars = max_cars
        self.water_capacity = water_capacity
        self.soap_capacity = soap_capacity
        self.price_per_class = price_per_class
        self.queue: list[Car] = []

    def add_car(self, car: Car) -> bool:
        if len(self.queue) >= self.max_cars:
            return False
        self.queue.append(car)
        return True

    def calculate_wash_cost(self, car: Car) -> float:
        return car.seats * self.price_per_class * int(car.comfort_class)

    def wash_car(self) -> float | None:
        if not self.queue:
            return None

        car = self.queue.pop(0)

        water_needed = car.seats * 0.5
        soap_needed = car.seats * 0.2

        if water_needed > self.water_capacity or soap_needed > self.soap_capacity:
            return None

        self.water_capacity -= water_needed
        self.soap_capacity -= soap_needed

        return self.calculate_wash_cost(car)

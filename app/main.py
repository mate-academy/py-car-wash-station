from typing import List


class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        model: str
    ) -> None:
        self.comfort_class: int = comfort_class
        self.clean_mark: int = clean_mark
        self.model: str = model


class CarWashStation:
    def __init__(
        self,
        bays: int,
        clean_power: int,
        price_per_unit: float,
        max_capacity: int
    ) -> None:
        self.bays: int = bays
        self.clean_power: int = clean_power
        self.price_per_unit: float = price_per_unit
        self.max_capacity: int = max_capacity
        self.cars_washed: int = 0
        self.average_rating: float = 0.0
        self.count_of_ratings: int = 0

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark >= self.clean_power:
            return 0.0
        price = self.price_per_unit * car.comfort_class
        car.clean_mark = self.clean_power
        self.cars_washed += 1
        return price

    def wash_single_car(self, car: Car) -> float:
        return self.calculate_washing_price(car)

    def serve_cars(self, cars: List[Car]) -> float:
        total_income = 0.0
        for car in cars:
            total_income += self.wash_single_car(car)
        return total_income

    def rate_service(self, mark: int) -> None:
        total = self.average_rating * self.count_of_ratings + mark
        self.count_of_ratings += 1
        self.average_rating = total / self.count_of_ratings

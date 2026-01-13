from typing import List


class Car:
    def __init__(
        self,
        comfort_class: int,
        cleanliness_mark: int,
        model: str
    ) -> None:
        self.comfort_class: int = comfort_class
        self.cleanliness_mark: int = cleanliness_mark
        self.model: str = model


class CarWashStation:
    def __init__(
        self,
        bays: int,
        water_liters: int,
        price_per_wash: float,
        max_capacity: int
    ) -> None:
        self.bays: int = bays
        self.water_liters: int = water_liters
        self.price_per_wash: float = price_per_wash
        self.max_capacity: int = max_capacity
        self.cars_washed: int = 0
        self.avg_rating: float = 0.0
        self.num_ratings: int = 0

    def calculate_washing_price(self, car: Car) -> float:
        if car.cleanliness_mark > 7:
            return 0.0
        price = self.price_per_wash * car.comfort_class
        return price

    def wash_single_car(self, car: Car) -> float:
        price = self.calculate_washing_price(car)
        if price > 0:
            self.cars_washed += 1
        return price

    def serve_cars(self, cars: List[Car]) -> float:
        total_income = 0.0
        for car in cars:
            total_income += self.wash_single_car(car)
        return total_income

    def rate_service(self, mark: int) -> None:
        total = self.avg_rating * self.num_ratings + mark
        self.num_ratings += 1
        self.avg_rating = total / self.num_ratings

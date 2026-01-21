from typing import List


class Car:
    def __init__(self, comfort_class: int, dirt_level: int, brand: str) -> None:
        self.comfort_class: int = comfort_class
        self.dirt_level: int = dirt_level
        self.brand: str = brand


class CarWashStation:
    def __init__(
        self,
        clean_power: int,
        max_cars: int,
        price_per_unit: float,
        efficiency: int,
    ) -> None:
        self.clean_power: int = clean_power
        self.max_cars: int = max_cars
        self.price_per_unit: float = price_per_unit
        self.efficiency: int = efficiency
        # Для рейтингу
        self.avg_rating: float = price_per_unit
        self.num_ratings: int = efficiency

    def wash_single_car(self, car: Car) -> float:
        if car.comfort_class >= self.clean_power:
            return 0.0
        car.comfort_class = max(car.comfort_class, self.clean_power)
        return self.calculate_washing_price(car)

    def calculate_washing_price(self, car: Car) -> float:
        # Не змінює car.comfort_class
        return car.comfort_class * self.price_per_unit

    def serve_cars(self, cars: List[Car]) -> float:
        total_income: float = 0.0
        for i, car in enumerate(cars):
            if i >= self.max_cars:
                break
            total_income += self.wash_single_car(car)
        return total_income

    def rate_service(self, mark: int) -> None:
        total = self.avg_rating * self.num_ratings + mark
        self.num_ratings += 1
        self.avg_rating = total / self.num_ratings

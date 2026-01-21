from typing import List


class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str) -> None:
        self.comfort_class = self.validate_parameter(comfort_class, 1, 7, 3)
        self.clean_mark = self.validate_parameter(clean_mark, 1, 10, 5)
        self.brand = brand

    @staticmethod
    def validate_parameter(
            value: int,
            min_value: int,
            max_value: int,
            default: int) -> int:
        if min_value <= value <= max_value:
            return value
        return default


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: int,
            count_of_ratings: int) -> None:
        self.distance_from_city_center = self.validate_parameter(
            distance_from_city_center, 0, float("inf"), 1.0
        )
        self.clean_power = self.validate_parameter(
            clean_power, 1, 10, 5
        )
        self.average_rating = self.validate_parameter(
            average_rating, 1, 5, 3
        )
        self.count_of_ratings = self.validate_parameter(
            count_of_ratings, 0, float("inf"), 0
        )

    @staticmethod
    def validate_parameter(
            value: float,
            min_value: float,
            max_value: float,
            default: float) -> float:
        if min_value <= value <= max_value:
            return value
        return default

    def serve_cars(self, cars: List[Car]) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = ((
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating)
            / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rating: float) -> None:
        self.average_rating = round(
            ((self.average_rating * self.count_of_ratings)
             + new_rating) / (self.count_of_ratings + 1), 1
        )
        self.count_of_ratings += 1

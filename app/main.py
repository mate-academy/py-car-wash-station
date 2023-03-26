from typing import Any


class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> Any:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: int,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> Any:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, cars: int) -> float:
        return round(
            (cars.comfort_class * (self.clean_power - cars.clean_mark)
             * self.average_rating) / self.distance_from_city_center, 1)

    def wash_single_car(self, car: int) -> int:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> float:
        result_cash = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                result_cash += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return result_cash

    def rate_service(self, rate: int) -> float:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rate)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

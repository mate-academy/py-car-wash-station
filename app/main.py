from typing import Callable, Any


class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:

        income = 0
        for clean_car in cars:
            if self.check_clean_mark_lower_then_power(clean_car):
                income += self.calculate_washing_price(clean_car)
                self.wash_single_car(clean_car)

        return income

    def calculate_washing_price(self, cars: Any) -> float:

        income = cars.comfort_class * (self.clean_power - cars.clean_mark)\
            * self.average_rating / self.distance_from_city_center

        return round(income, 1)

    def check_clean_mark_lower_then_power(self, сar: Any) -> None:
        return сar.clean_mark < self.clean_power

    def wash_single_car(self, сar: Callable) -> None:

        if self.check_clean_mark_lower_then_power(Car):
            сar.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        self.count_of_ratings += 1
        self.average_rating = round((self.average_rating
                                    * (self.count_of_ratings - 1) + rate)
                                    / self.count_of_ratings, 1)

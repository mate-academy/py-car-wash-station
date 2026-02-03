from typing import List


class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class: int = comfort_class
        self.clean_mark: int = clean_mark
        self.brand: str = brand


class CarWashStation:
    """Car wash station class with methods to serve cars and rate service."""

    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center: float = distance_from_city_center
        self.clean_power: int = clean_power
        self.average_rating: float = average_rating
        self.count_of_ratings: int = count_of_ratings

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculate the cost for a single car wash.
        Formula:
        comfort_class * (clean_power - car.clean_mark) * average_rating /
        distance_from_city_center
        Returns rouded result (1 decimal).
        """
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def serve_cars(self, cars: List[Car]) -> float:
        """
        Takes a list of Car objects, washes only cars with clean_mark less than
        the clean_power of the wash station, and returns total income rounded
        to 1 decimal.
        """
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, rate: float) -> None:
        """
        Adds a single rate to the wash station and updates
        average_rating and count_of_ratings.
        """
        new_average = (
            self.average_rating * self.count_of_ratings + rate
        ) / (self.count_of_ratings + 1)
        self.average_rating = round(new_average, 1)
        self.count_of_ratings += 1

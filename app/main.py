from __future__ import annotations


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
        income = sum([
            self.calculate_washing_price(car)
            for car in cars
            if car.clean_mark < self.clean_power
        ])

        [
            self.wash_single_car(car)
            for car in cars
            if car.clean_mark < self.clean_power
        ]

        return income

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center,
            1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        new_rating = (self.average_rating * self.count_of_ratings + rating) / \
                     (self.count_of_ratings + 1)
        self.average_rating = round(new_rating, 1)
        self.count_of_ratings += 1

from __future__ import annotations
from typing import List


class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str,
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: int | float,
        clean_power: int | float,
        average_rating: int | float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def __str__(self) -> str:
        return (
            f"Distance: {self.distance_from_city_center} km, "
            f"Power: {self.clean_power}, "
            f"Rating: {self.average_rating}, "
            f"Count of ratings: {self.count_of_ratings}"
        )

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            (
                car.comfort_class
                * (self.clean_power - car.clean_mark)
                * self.average_rating
            )
            / self.distance_from_city_center,
            1,
        )

    def rate_service(self, rating: int | float) -> None:
        new_rating = (
            (self.average_rating * (self.count_of_ratings)) + rating
        )
        self.count_of_ratings += 1

        self.average_rating = round(
            new_rating
            / self.count_of_ratings,
            1,
        )

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def cars_to_serve(self, cars: List[Car]) -> List[Car]:
        return [car for car in cars if car.clean_mark < self.clean_power]

    def serve_cars(self, cars: List[Car]) -> float:
        cars_to_serve = self.cars_to_serve(cars)

        income = 0
        for car in cars_to_serve:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return round(income, 1)

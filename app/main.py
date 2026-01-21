from __future__ import annotations


def limitation(
        num: int | float,
        min_lim: int | float,
        max_lim: int | float
) -> int | float:
    if num < min_lim:
        return min_lim
    elif num > max_lim:
        return max_lim
    return num


class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class = limitation(comfort_class, 1, 7)
        self.clean_mark = limitation(clean_mark, 1, 10)
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = limitation(
            distance_from_city_center, 1.0, 10.0
        )
        self.clean_power = limitation(clean_power, 1, 10)
        self.average_rating = round(limitation(average_rating, 1.0, 5.0), 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for index, car in enumerate(cars):
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(cars[index])
                self.wash_single_car(cars[index])
        return income

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center,
            1
        )

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        self.average_rating = round(
            (self.average_rating
             * self.count_of_ratings + rate)
            / (self.count_of_ratings + 1),
            1
        )
        self.count_of_ratings += 1

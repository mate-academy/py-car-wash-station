from __future__ import annotations

from dataclasses import dataclass
from typing import Type


@dataclass
class Validator:
    min_value: int
    max_value: int

    def __set_name__(self, owner: Type, name: str) -> None:
        self.protected_name = f"_{name}"

    def __get__(self, instance: object, owner: Type) -> Type:
        return getattr(instance, self.protected_name, None)

    def __set__(self, instance: Type, value: float) -> None:
        if not self.min_value <= value <= self.max_value:
            raise ValueError(f"value = {value} must be in range: "
                             f"{self.min_value} and {self.max_value}")
        setattr(instance, self.protected_name, value)


@dataclass
class Car:
    comfort_class: float = Validator(1, 7)
    clean_mark: int = Validator(1, 10)
    brand: str = None


@dataclass
class CarWashStation:
    distance_from_city_center: float = Validator(1, 10)
    clean_power: int = None
    average_rating: float = Validator(1, 5)
    count_of_ratings: int = None

    def wash_single_car(self, one_car: Car) -> float:
        if self.clean_power > one_car.clean_mark:
            price = self.calculate_washing_price(one_car)
            one_car.clean_mark = self.clean_power
            return price
        return 0.0

    def calculate_washing_price(self, car: Car) -> float:
        price = ((car.comfort_class
                  * (self.clean_power - car.clean_mark)
                  * self.average_rating)
                 / self.distance_from_city_center)

        return round(price, 1)

    def serve_cars(self, car_list: list[Car]) -> int:
        return sum(self.wash_single_car(car) for car in car_list)

    def rate_service(self, rate: int) -> None:
        rating = (((self.average_rating
                    * self.count_of_ratings) + rate)
                  / (self.count_of_ratings + 1))
        self.average_rating = round(rating, 1)
        self.count_of_ratings += 1


def main() -> None:
    pass


if __name__ == "__main__":
    try:
        main()
    except ValueError as e_info:
        print(e_info)

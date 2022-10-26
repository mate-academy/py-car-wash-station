from typing import Union
from typing import List


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

    def serve_cars(self, list_of_cars: List[Car]) -> float:
        income = 0
        for car in list_of_cars:
            income += self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
            , 1
        )

    def wash_single_car(self, car: Car) -> float:
        income = 0
        if self.clean_power > car.clean_mark:
            income = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
        return income

    def rate_service(self, rating: Union[int, float]) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rating)
            / (self.count_of_ratings + 1)
            , 1
        )
        self.count_of_ratings += 1

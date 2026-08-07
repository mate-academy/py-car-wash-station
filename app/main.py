from typing import Any


class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> Any:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: float,
            average_rating: float,
            count_of_ratings: int,
    ) -> Any:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, cars: Car) -> float:
        return round(
            cars.comfort_class
            * (self.clean_power - cars.clean_mark)
            * self.average_rating / self.distance_from_city_center,
            1,
        )

    def serve_cars(self, cars: Car) -> float:
        result_price = 0
        for i in cars:
            if i.clean_mark < self.clean_power:
                result_price += self.calculate_washing_price(i)
                self.wash_single_car(i)
        return round(result_price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, mark: int) -> None:
        self.average_rating = round(
            (
                self.average_rating * self.count_of_ratings + mark
            ) / (self.count_of_ratings + 1),
            1,
        )
        self.count_of_ratings = self.count_of_ratings + 1

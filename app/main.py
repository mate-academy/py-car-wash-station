from typing import Any


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
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> int:
        income = sum([car.clean_mark
                      for car in cars
                      if car.clean_mark < self.clean_power])
        return round(income, 1)

    def calculate_washing_price(self, car: Any) -> None:
        single_car_wash = \
            (
                car.comfort_class * self.clean_power - car.clean_mark
                * self.average_rating / self.distance_from_city_center
            )
        return round(single_car_wash, 1)

    def wash_single_car(self, car: Any) -> Any:
        if self.clean_power > car.clean_mark:
            car.clean_mark == self.clean_power
            return True
        else:
            return False

    def rate_service(self, new_rating: int) -> Any:
        self.count_of_ratings += 1
        self.average_rating = round(
            (self.average_rating + new_rating)
            / self.count_of_ratings, 1
        )

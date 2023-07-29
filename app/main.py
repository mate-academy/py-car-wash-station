from typing import Any


class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> Any:
        digit = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                digit += round(self.calculate_washing_price(car), 1)
                self.wash_single_car(car)
        return digit

    def calculate_washing_price(self, car: Any) -> Any:
        result = \
            car.comfort_class * \
            (self.clean_power - car.clean_mark)\
            * self.average_rating / self.distance_from_city_center
        return result

    def wash_single_car(self, car: Any) -> Any:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
            return car.clean_mark

    def rate_service(self, rate: int) -> Any:
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += rate
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)
        return self.average_rating

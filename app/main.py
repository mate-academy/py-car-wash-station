from typing import Any


class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> Any:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: Any,
                 average_rating: float, count_of_ratings: Any) -> Any:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: object) -> Any:
        if car.clean_mark < self.clean_power:
            price = (
                car.comfort_class
                * (self.clean_power - car.clean_mark)
                * self.average_rating
                / self.distance_from_city_center
            )
            return round(price, 1)
        return 0

    def wash_single_car(self, car: object) -> Any:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
            return car.clean_mark

    def rate_service(self, rating: float) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round((total_rating + rating) / self.count_of_ratings, 1)
        return self.count_of_ratings, self.average_rating

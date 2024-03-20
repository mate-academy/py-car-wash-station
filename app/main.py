from typing import Any


class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Any) -> float:
        price = 0
        if car.clean_mark < self.clean_power:
            price += (car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating) / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Any) -> int:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
            print(car.clean_mark)
        return car.clean_mark

    def serve_cars(self, queue: Any) -> float:
        income = 0
        for car in queue:
            if car.clean_mark < self.clean_power:
                income += (car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating) / self.distance_from_city_center
                self.wash_single_car(car)
        return round(income, 1)

    def rate_service(self, mark: int) -> tuple:
        self.average_rating = round((self.average_rating * self.count_of_ratings + mark) / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
        return self.average_rating, self.count_of_ratings

from typing import Callable


class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> Callable:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int,
                 clean_power: int,
                 average_rating: int,
                 count_of_ratings: int) -> Callable:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars_list: list) -> int:
        result = 0
        for i in cars_list:
            if i.clean_mark < self.clean_power:
                result += self.calculate_washing_price(i)
                self.wash_single_car(i)
        return result

    def calculate_washing_price(self, car: Callable) -> Callable:

        income = round(
            ((car.comfort_class * (self.clean_power - car.clean_mark)
              * self.average_rating) / self.distance_from_city_center), 1
        )
        return income

    def wash_single_car(self, car: Callable) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        self.average_rating = round(
            ((self.average_rating * self.count_of_ratings) + rating)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

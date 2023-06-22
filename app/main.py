from typing import Any


class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int
                 ) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        total_price = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_price += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return total_price

    def calculate_washing_price(self, car: Any) -> float:
        price = car.comfort_class * \
            ((self.clean_power - car.clean_mark)
                * self.average_rating / self.distance_from_city_center)

        return round(price, 1)

    def wash_single_car(self, car: str) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = round(self.clean_power, 1)

    def rate_service(self, rate: float) -> float:
        all_rates = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round((all_rates + rate)
                                    / self.count_of_ratings, 1)

        return self.average_rating

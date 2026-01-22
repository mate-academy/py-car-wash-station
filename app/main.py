from typing import List


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
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        clean_price_part = self.clean_power - car.clean_mark
        station_price_part = (
            self.average_rating / self.distance_from_city_center
        )
        price = car.comfort_class * clean_price_part * station_price_part
        return round(price, 1)

    def rate_service(self, new_rating: float) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = (
            round((total_rating + new_rating) / self.count_of_ratings, 1)
        )

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
        return income

    def calculate_washing_price(self, car: Car) -> float:
        amount = self.clean_power - car.clean_mark
        extra_rate = self.average_rating / self.distance_from_city_center
        price = car.comfort_class * amount * extra_rate
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> (float, int):
        all_of_rate = self.count_of_ratings * self.average_rating + rate
        self.average_rating = round(all_of_rate
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

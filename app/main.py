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

    def serve_cars(self, car: List[Car]) -> float:
        total_income = 0
        for item in car:
            if item.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(item)
                self.wash_single_car(item)
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        income = car.comfort_class * (self.clean_power - car.clean_mark) \
            * self.average_rating / self.distance_from_city_center
        return round(income, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, single_rate: int) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + single_rate)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

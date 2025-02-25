from typing import List


class Car:
    def __init__(self
                 , comfort_class: int
                 , clean_mark: int
                 , brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self
                 , distance_from_city_center: float
                 , clean_power: int
                 , average_rating: float
                 , count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        dist = self.distance_from_city_center
        if dist == 0:
            dist = 1.0
        return ((car.comfort_class * (self.clean_power - car.clean_mark)
                 * self.average_rating) / dist)

    def wash_single_car(self, car: Car) -> float:
        income = 0
        if self.clean_power > car.clean_mark:
            income = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power

        return round(income, 1)

    def serve_cars(self, cars: List[Car]) -> float:
        income = 0.0
        for car in cars:
            income += self.wash_single_car(car)

        return round(income, 1)

    def rate_service(self, num: float) -> None:
        self.average_rating = round((self.average_rating
                                    * self.count_of_ratings + num)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

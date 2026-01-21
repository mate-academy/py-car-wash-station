from typing import List


class Car:

    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self. brand = brand


class CarWashStation:

    def __init__(
            self,
            distance_from_the_city_center: float,
            clean_power: int, average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_the_city_center = distance_from_the_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        wash_car = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                wash_car += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(wash_car, 1)

    def calculate_washing_price(self, car: Car) -> float:
        wash_price = car.comfort_class * (self.clean_power - car.clean_mark) \
            * (self.average_rating / self.distance_from_the_city_center)
        return round(wash_price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rate)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

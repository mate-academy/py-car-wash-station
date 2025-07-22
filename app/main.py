from typing import List


class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
        self.total_income = 0

    def wash_single_car(self, car: Car) -> float:
        cost = 0
        if car.clean_mark < self.clean_power:
            cost = (car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating) / self.distance_from_city_center
            car.clean_mark = self.clean_power
        self.total_income += cost
        return self.total_income

    def serve_cars(self, cars: List[Car]) -> float:
        cost = 0
        for car in cars:
            self.wash_single_car(car)
        self.total_income += cost
        return round(self.total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        return (car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating) / self.distance_from_city_center

    def rate_service(self, rate: int) -> None:
        rating = round((self.average_rating * self.count_of_ratings + rate) / (self.count_of_ratings + 1), 1)
        self.average_rating = rating
        self.count_of_ratings += 1

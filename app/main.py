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
                 clean_power: float,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        income = 0.0
        for car in cars:
            income += self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        comfort_factor = car.comfort_class
        cleanliness_factor = self.clean_power - car.clean_mark
        location_factor = self.average_rating / self.distance_from_city_center

        washing_price = comfort_factor * cleanliness_factor * location_factor
        return round(washing_price, 1)

    def rate_service(self, rate: int) -> float:
        total_rating = self.average_rating * self.count_of_ratings + rate
        new_count = self.count_of_ratings + 1
        self.average_rating = round(total_rating / new_count, 1)
        self.count_of_ratings = new_count
        return self.average_rating

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price

        return 0.0

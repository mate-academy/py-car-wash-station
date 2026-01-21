from typing import List


class Car:
    def __init__(self, comfort_class: int = 1,
                 clean_mark: int = 1,
                 brand: str = "") -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float = 1.0,
                 clean_power: int = 1,
                 average_rating: float = 1.0,
                 count_of_ratings: int = 1) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class
                     * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 1)

    def serve_cars(self, cars: List[Car]) -> float:
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                come_one = self.calculate_washing_price(car)
                total_income += come_one
                car.clean_mark = self.clean_power
                self.wash_single_car(car)
        return round(total_income, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rating: float) -> None:
        self.average_rating = (
            self.average_rating * self.count_of_ratings + new_rating
        ) / (self.count_of_ratings + 1)
        self.count_of_ratings += 1
        self.average_rating = round(self.average_rating, 1)

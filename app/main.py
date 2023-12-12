from typing import List


class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, dfcc: float, cp: int, ar: float, cor: int) -> None:
        self.dist_cent = dfcc
        self.clean_power = cp
        self.average_rating = ar
        self.count_of_ratings = cor

    def serve_cars(self, cars: List[Car]) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        comfort_diff = self.clean_power - car.clean_mark
        price = (car.comfort_class * comfort_diff * self.average_rating)
        price /= self.dist_cent
        result = round(price, 1)
        return result

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        rating_sum = self.average_rating * self.count_of_ratings + rating
        new_count = self.count_of_ratings + 1
        self.average_rating = round(rating_sum / new_count, 1)
        self.count_of_ratings += 1

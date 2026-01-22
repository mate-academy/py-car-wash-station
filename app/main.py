from __future__ import annotations


class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int,
                 clear_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clear_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                total_income += self.calculate_washing_price(car)
                car.clear_mark = self.clean_power
                self.wash_single_car(car)
        return total_income

    def calculate_washing_price(self, car: Car) -> float:
        price = (car.comfort_class * (self.clean_power - car.clean_mark) * (
                 self.average_rating / self.distance_from_city_center))
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> float:
        rating = self.count_of_ratings * self.average_rating
        self.count_of_ratings += 1
        rating += rate
        self.average_rating = round(rating / self.count_of_ratings, 1)
        return self.average_rating

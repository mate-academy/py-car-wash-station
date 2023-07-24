from typing import List


class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: float,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: float,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: List[Car]) -> float:
        total_income = 0.0

        for car in car_list:
            if car.clean_mark < self.clean_power:
                cost = self.calculate_washing_price(car)
                total_income += cost
                self.wash_single_car(car)

        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        difference = self.clean_power - car.clean_mark
        remainder = self.average_rating / self.distance_from_city_center
        result_price = car.comfort_class * difference * remainder
        return round(result_price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> float:
        if 1.0 <= rating <= 5.0:
            total_rating = self.average_rating * self.count_of_ratings
            self.count_of_ratings += 1
            total_rating += rating
            self.average_rating = total_rating / self.count_of_ratings
            self.average_rating = round(self.average_rating, 1)
            return self.average_rating

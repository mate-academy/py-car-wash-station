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
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car_for_wash: Car) -> float:
        comfy_class = car_for_wash.comfort_class
        clean_difference = self.clean_power - car_for_wash.clean_mark
        rating = self.average_rating
        distance = self.distance_from_city_center
        price = round(comfy_class * clean_difference * rating / distance, 1)
        return price

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, line_of_cars: List[Car]) -> float:
        serve_income = 0
        for car in line_of_cars:
            if self.clean_power > car.clean_mark:
                serve_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return serve_income

    def rate_service(self, mark: float) -> None:
        total_mark = self.average_rating * self.count_of_ratings + mark
        total_count = self.count_of_ratings + 1
        self.average_rating = round(total_mark / total_count, 1)
        self.count_of_ratings += 1

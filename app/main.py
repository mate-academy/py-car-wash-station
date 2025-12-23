from typing import List


class Car:
    def __init__(
            self: "Car",
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self: "CarWashStation",
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self: "CarWashStation", car: Car) -> float:
        if car.clean_mark >= self.clean_power:
            return 0.0
        diff = self.clean_power - car.clean_mark
        cost = (
            car.comfort_class * diff * self.average_rating
        ) / self.distance_from_city_center
        return round(cost, 1)

    def wash_single_car(self: "CarWashStation", car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self: "CarWashStation", cars: List[Car]) -> float:
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self: "CarWashStation", new_rate: int) -> None:
        total = self.average_rating * self.count_of_ratings + new_rate
        self.count_of_ratings += 1
        self.average_rating = round(total / self.count_of_ratings, 1)

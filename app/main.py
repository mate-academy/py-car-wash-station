from typing import List


class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:

        self.comfort_class = max(1, min(comfort_class, 7))
        self.clean_mark = max(0, min(clean_mark, 10))
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:

        self.distance_from_city_center = max(
            1.0, min(distance_from_city_center, 10.0)
        )
        self.clean_power = max(1, min(clean_power, 10))
        self.average_rating = round(max(1.0, min(average_rating, 5.0)), 1)
        self.count_of_ratings = max(count_of_ratings, 0)

    def serve_cars(self, cars: List[Car]) -> float:
        total_income = sum(
            self.wash_single_car(car)
            for car in cars
            if car.clean_mark < self.clean_power
        )
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        if not isinstance(car, Car):
            raise ValueError("The argument must be a Car instance")

        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center, 1
        )

    def wash_single_car(self, car: Car) -> float:
        if not isinstance(car, Car):
            raise ValueError("The argument must be a Car instance")

        if car.clean_mark < self.clean_power:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price

    def rate_service(self, new_rating: float) -> None:
        if not (1.0 <= new_rating <= 5.0):
            raise ValueError("new_rating must be between 1.0 and 5.0")

        self.count_of_ratings += 1
        self.average_rating = round(
            ((self.average_rating * (self.count_of_ratings - 1)) + new_rating)
            / self.count_of_ratings, 1
        )

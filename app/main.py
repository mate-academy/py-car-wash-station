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
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings
        self.reviews: List[float] = []

    def serve_cars(self, cars: List[Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark >= self.clean_power:
            return 0.0
        price = (car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating) / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = max(car.clean_mark, self.clean_power)

    def rate_service(self, rate: float) -> None:
        self.count_of_ratings += 1
        self.average_rating = round(
            (self.average_rating * (self.count_of_ratings - 1) + rate) / self.count_of_ratings, 1
        )
        self.reviews.append(rate)

    def get_rating(self) -> float:
        return self.average_rating

    def add_review(self, rate: float) -> None:
        self.rate_service(rate)

    def get_review_count(self) -> int:
        return self.count_of_ratings

    def get_reviews(self) -> List[float]:
        return self.reviews.copy()
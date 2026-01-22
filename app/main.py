from typing import List


class Car:
    def __init__(
        self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:
        self.comfort_class: int = comfort_class
        self.clean_mark: int = clean_mark
        self.brand: str = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: int,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center: int = distance_from_city_center
        self.clean_power: int = clean_power
        self.average_rating: float = average_rating
        self.count_of_ratings: int = count_of_ratings

    def serve_car(self, car: Car) -> float:
        if car.comfort_class <= self.distance_from_city_center:
            price: float = car.comfort_class * 11
            price *= self.clean_power / 5
            if car.clean_mark < self.clean_power:
                car.clean_mark = self.clean_power
            return round(price, 2)
        return 0.0

    def serve_cars(self, cars: List[Car]) -> float:
        total: float = 0.0
        for car in cars:
            total += self.serve_car(car)
        return round(total, 2)

    def rate_service(self, new_rating: int) -> None:
        total_rating: float = self.average_rating * self.count_of_ratings
        total_rating += new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)

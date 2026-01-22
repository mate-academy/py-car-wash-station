from typing import List


class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str,
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

    def _needed_diff(self, car: Car) -> int:
        return max(self.clean_power - car.clean_mark, 0)

    def calculate_washing_price(self, car: Car) -> float:
        diff = self._needed_diff(car)
        if diff == 0:
            return 0.0
        ratio = self.average_rating / self.distance_from_city_center
        price = car.comfort_class * diff * ratio
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: List[Car]) -> float:
        total = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total, 1)

    def rate_service(self, new_rating: float) -> None:
        total = self.average_rating * self.count_of_ratings + new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total / self.count_of_ratings, 1)

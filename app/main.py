from typing import List, Optional


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
        clean_power: float,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                original_clean_mark = car.clean_mark
                self.wash_single_car(car)
                income += self.calculate_washing_price(
                    car, original_clean_mark
                )
        return round(income, 1)

    def calculate_washing_price(
        self,
        car: Car,
        original_clean_mark: Optional[int] = None
    ) -> float:
        if original_clean_mark is None:
            original_clean_mark = car.clean_mark
        if original_clean_mark >= self.clean_power:
            return 0
        price = (
            car.comfort_class
            * (self.clean_power - original_clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rating: float) -> None:
        if 1.0 <= new_rating <= 5.0:
            total_rating = (
                self.average_rating * self.count_of_ratings + new_rating
            )
            self.count_of_ratings += 1
            self.average_rating = round(
                total_rating / self.count_of_ratings, 1
            )

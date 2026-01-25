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
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center: float = distance_from_city_center
        self.clean_power: int = clean_power
        self.average_rating: float = round(average_rating, 1)
        self.count_of_ratings: int = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        diff: int = self.clean_power - car.clean_mark

        cost: float = (
            (car.comfort_class * diff * self.average_rating)
            / self.distance_from_city_center
        )

        return round(cost, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: List[Car]) -> float:
        income: float = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price: float = self.calculate_washing_price(car)
                income += price
                self.wash_single_car(car)

        return round(income, 1)

    def rate_service(self, new_rate: int) -> None:
        total_score: float = self.average_rating * self.count_of_ratings
        total_score += new_rate
        self.count_of_ratings += 1
        self.average_rating = round(total_score / self.count_of_ratings, 1)

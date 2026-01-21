from typing import List


class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str
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
        self.average_rating: float = average_rating
        self.count_of_ratings: int = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        income: float = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price: float = self.calculate_washing_price(car)
                income += price
                car.clean_mark = self.clean_power
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price: float = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> float:
        old_average: float = self.average_rating
        old_count: int = self.count_of_ratings
        new_average: float = (old_average * old_count + rate) / (old_count + 1)
        self.average_rating = round(new_average, 1)
        self.count_of_ratings += 1
        return self.average_rating

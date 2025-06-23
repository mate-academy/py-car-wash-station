from typing import List


class Car:

    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
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
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        sum_of_costs = 0

        for car in cars:
            if self.is_washable(car):
                sum_of_costs += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(sum_of_costs, 1)

    def calculate_washing_price(self, car: Car) -> float:
        difference_between_clean_power_and_mark = self.clean_power - car.clean_mark
        result = (
            car.comfort_class
            * difference_between_clean_power_and_mark
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(result, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.is_washable(car):
            car.clean_mark = self.clean_power

    def rate_service(self, mark: int) -> None:
        sum_of_marks = self.count_of_ratings * self.average_rating
        sum_of_marks += mark
        self.count_of_ratings += 1
        self.average_rating = round(sum_of_marks / self.count_of_ratings, 1)

    def is_washable(self, car: Car) -> bool:
        return self.clean_power > car.clean_mark

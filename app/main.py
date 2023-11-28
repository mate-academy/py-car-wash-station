from typing import Any


class Car:
    def __init__(
            self, comfort_class: int, clean_mark: int, brand: str) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(
            self: Any, distance_from_city_center: int, clean_power: int,
            average_rating: float, count_of_ratings:
            int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        result = 0
        # __________________________compliance check on clean_power
        for car in cars:
            if car.clean_mark < self.clean_power:
                result += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(result, 1)

        # __________________________wash single car
    def wash_single_car(self, mark: Any) -> float:
        mark.clean_mark = self.clean_power

    # ___________________________calculate price per car
    def calculate_washing_price(self, mark: Any) -> float:
        cost = ((mark.comfort_class
                 * (self.clean_power - mark.clean_mark)
                * self.average_rating) / self.distance_from_city_center)

        return round(cost, 1)

    # ___________________________calculate rating
    def rate_service(self, single_rate: float) -> float:
        rating = round(
            (self.average_rating * self.count_of_ratings + single_rate)
            / (self.count_of_ratings + 1), 1)

        self.count_of_ratings += 1
        self.average_rating = rating
        return rating

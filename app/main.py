from typing import List


class Car:
    def __init__(
        self, comfort_class: int, clean_mark: int, brand: str
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
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        total_profit = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                total_profit += self.calculate_washing_price(car=car)
                self.wash_single_car(car=car)

        return round(total_profit, 1)

    def calculate_washing_price(self, car: Car) -> float:
        calculate_difference_of_power = self.clean_power - car.clean_mark
        divine_rating_and_distance = (
            self.average_rating / self.distance_from_city_center
        )
        total_calculating = round(
            (
                car.comfort_class
                * calculate_difference_of_power
                * divine_rating_and_distance
            ),
            1,
        )

        return total_calculating

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark: int) -> None:
        calculate_mark = self.average_rating * self.count_of_ratings

        updated_rating = round(
            (calculate_mark + mark) / (self.count_of_ratings + 1), 1
        )

        self.average_rating = updated_rating
        self.count_of_ratings += 1

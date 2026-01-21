from __future__ import annotations


class Car:

    def __init__(
            self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: float) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: Car) -> Car:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
            return car.comfort_class, car.clean_mark, car.brand

    def calculate_washing_price(self, car: Car) -> float:
        washing_result = self.clean_power - car.clean_mark
        return round(
            car.comfort_class * washing_result
            * self.average_rating
            / self.distance_from_city_center, 1
        )

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
                car = self.wash_single_car(car)
        return income

    def rate_service(self, new_rate: float) -> CarWashStation:
        total_rates_before_new_rate = \
            self.average_rating * self.count_of_ratings
        new_count_of_ratings = self.count_of_ratings + 1
        new_average_rating = round(
            (total_rates_before_new_rate + new_rate)
            / new_count_of_ratings, 1
        )
        self.average_rating = new_average_rating
        self.count_of_ratings = new_count_of_ratings
        return self.distance_from_city_center, self.clean_power, \
            self.average_rating, self.count_of_ratings

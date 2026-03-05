from __future__ import annotations


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
        self.distance_from_city_center = float(distance_from_city_center)
        self.clean_power = clean_power
        self.average_rating = round(float(average_rating), 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0.0

        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark >= self.clean_power:
            return 0.0

        clean_difference = self.clean_power - car.clean_mark
        raw_cost = (
            car.comfort_class
            * clean_difference
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(raw_cost, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark: int) -> None:
        total_rating_sum = self.average_rating * self.count_of_ratings
        new_count = self.count_of_ratings + 1
        new_average = (total_rating_sum + mark) / new_count

        self.count_of_ratings = new_count
        self.average_rating = round(new_average, 1)

from __future__ import annotations


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

    def wash_single_car(self, car: Car) -> None:
        """Washes the car only if its clean_mark is below clean_power."""
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculate the wash price WITHOUT modifying the car.

        Formula (exactly as required):
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center

        Returns the result rounded to 1 decimal place.
        """
        if car.clean_mark >= self.clean_power:
            return 0.0

        diff = self.clean_power - car.clean_mark
        raw_cost = (
            car.comfort_class
            * diff
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(raw_cost, 1)

    def serve_cars(self, cars: list[Car]) -> float:
        """Wash eligible cars """
        total_income: float = 0.0

        for car in cars:
            price = self.calculate_washing_price(car)
            if price > 0:
                total_income += price
            self.wash_single_car(car)

        return round(total_income, 1)

    def rate_service(self, mark: int) -> None:
        """Add one new customer"""
        total_before = self.average_rating * self.count_of_ratings
        new_total = total_before + mark
        self.count_of_ratings += 1
        self.average_rating = round(
            new_total / self.count_of_ratings,
            1
        )

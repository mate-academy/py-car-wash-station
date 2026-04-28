from typing import List


class Car:
    """Represents a car."""

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
    """Represents a car wash station."""

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

    def calculate_washing_price(self, car: Car) -> float:
        """Calculate washing price for a single car."""
        if car.clean_mark >= self.clean_power:
            return 0.0

        diff = self.clean_power - car.clean_mark
        price = (
            car.comfort_class
            * diff
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> float:
        """Wash a single car if possible and return the price."""
        if car.clean_mark < self.clean_power:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price

        return 0.0

    def serve_cars(self, cars: List[Car]) -> float:
        """Wash eligible cars and return total income."""
        income = 0.0

        for car in cars:
            income += self.wash_single_car(car)

        return round(income, 1)

    def rate_service(self, new_rate: float) -> None:
        """Add a new rating and update the average."""
        total_score = (
            self.average_rating * self.count_of_ratings + new_rate
        )
        self.count_of_ratings += 1
        self.average_rating = round(
            total_score / self.count_of_ratings, 1
        )

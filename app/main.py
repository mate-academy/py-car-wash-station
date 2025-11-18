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
        comfort_class: int,
        clear_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.comfort_class: int = comfort_class
        self.clear_power: int = clear_power
        self.average_rating: float = average_rating
        self.count_of_ratings: int = count_of_ratings

    def wash_single_car(self, car: Car) -> None:
        """Wash the car by raising clean_mark up to clear_power."""
        if car.clean_mark < self.clear_power:
            car.clean_mark = self.clear_power

    def calculate_washing_price(self, car: Car) -> float:
        """
        Return price of washing a single car.
        0 if car is already clean enough (clean_mark >= clear_power).
        """
        if car.clean_mark >= self.clear_power:
            return 0.0

        return float(car.comfort_class * self.average_rating)

    def serve_cars(self, cars: list[Car]) -> float:
        """Wash all cars and return total revenue."""
        total_income: float = 0.0

        for car in cars:
            total_income += self.calculate_washing_price(car)
            self.wash_single_car(car)

        return round(total_income, 1)

    def rate_service(self, mark: int) -> None:
        """Add a new rating and update average_rating."""
        new_total = self.average_rating * self.count_of_ratings + mark
        self.count_of_ratings += 1
        self.average_rating = round(new_total / self.count_of_ratings, 1)

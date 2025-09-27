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
        clean_power: float,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        # store average rating rounded to 1 decimal as required
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """
        Cost formula:
        comfort_class * (clean_power - car.clean_mark) * average_rating / distance
        Returned rounded to 1 decimal. If no cleaning needed (diff <= 0), returns 0.0.
        """
        diff = self.clean_power - car.clean_mark
        if diff <= 0:
            return 0.0
        price = (
            car.comfort_class * diff * self.average_rating / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """Wash a single car to 'clean_power' if it is below that."""
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: List[Car]) -> float:
        """
        Wash cars with clean_mark < clean_power.
        Sum the per-car prices (each already rounded to 1 decimal).
        Return total rounded to 1 decimal.
        """
        total = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                # per-car price must be rounded individually to match example totals
                price = self.calculate_washing_price(car)
                total += price
                # then actually wash the car
                self.wash_single_car(car)
        return round(total, 1)

    def rate_service(self, rate: float) -> None:
        """
        Add a single rate and update average_rating (rounded to 1 decimal)
        and count_of_ratings.
        """
        total_sum = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(total_sum / self.count_of_ratings, 1)

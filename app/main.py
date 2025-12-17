from typing import Any


class Car:
    """
    Represents a vehicle to be processed by the car wash station,
    storing its comfort class, brand, and current cleanliness state.
    """

    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    """
    Represent a car wash station that processes multiple cars
    and manages ratings. If the distance is invalid, the distance is always 1.0
    """

    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        if distance_from_city_center <= 0:
            self.distance_from_city_center = 1.0
        else:
            self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        """
        Wash a list of cars, update their cleanliness if the clean mark
        is less than the clean power of the station, and return total income.
        """
        income = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Any) -> float:
        """
        Calculate the cost of washing a single car based on station and
        car attributes and round the result with 1 decimal.
        """
        clean_car_rest = self.clean_power - car.clean_mark
        wash_car = car.comfort_class * clean_car_rest * self.average_rating

        return round(wash_car / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Any) -> None:
        """
        Update the clean mark of the washed car if required.
        """
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> float:
        """
        Add a new rating and update the station's average rating
        rounding the result with 1 decimal.
        """
        prev_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round(
            (prev_rating + rating) / self.count_of_ratings, 1)
        return self.average_rating

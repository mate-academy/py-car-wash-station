"""
Car Wash Station Management System

This module provides classes for managing cars and car wash stations.
It handles car washing operations, pricing calculations, and service
ratings.
"""

from typing import List


class Car:
    """
    Represents a car that can be washed at a car wash station.

    Attributes:
        comfort_class (int): The comfort class of the car (affects pricing)
        clean_mark (int): Current cleanliness level of the car (0-10)
        brand (str): Brand/manufacturer of the car
    """

    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        """
        Initialize a new Car instance.

        Args:
            comfort_class: Comfort class of the car (higher = more expensive)
            clean_mark: Current cleanliness level (0-10, where 0 is dirty,
                       10 is clean)
            brand: Brand name of the car
        """
        self.brand = brand
        self.clean_mark = clean_mark
        self.comfort_class = comfort_class


class CarWashStation:
    """
    Represents a car wash station that can serve multiple cars.

    The station calculates washing prices based on car comfort class,
    cleanliness difference, average rating, and distance from city center.
    """

    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        """
        Initialize a new CarWashStation instance.

        Args:
            distance_from_city_center: Distance from city center in kilometers
            clean_power: Maximum cleanliness level the station can achieve (0-10)
            average_rating: Current average service rating (0-10)
            count_of_ratings: Total number of ratings received
        """
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        """
        Serve a list of cars and return total revenue.

        Args:
            cars: List of Car objects to be served

        Returns:
            Total price earned from serving all eligible cars
        """
        total_price = 0.0

        for car in cars:
            if self.can_serve(car):
                price = self.calculate_washing_price(car)
                total_price += price
                self.wash_single_car(car)
            else:
                print(f"Car {car.brand} cannot be served")

        return total_price

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculate the price for washing a specific car.

        Formula: comfort_class * (clean_power - clean_mark) * average_rating
                / distance

        Args:
            car: Car object to calculate price for

        Returns:
            Washing price rounded to 1 decimal place
        """
        cleanliness_difference = self.clean_power - car.clean_mark
        base_price = car.comfort_class * cleanliness_difference
        adjusted_price = (base_price * self.average_rating /
                         self.distance_from_city_center)

        return round(adjusted_price, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        Wash a single car, updating its cleanliness level.

        Args:
            car: Car object to wash
        """
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        """
        Add a new rating and update the average rating.

        Args:
            rating: New rating value (0-10)
        """
        if not (0 <= rating <= 10):
            raise ValueError("Rating must be between 0 and 10")

        # Calculate new average rating
        total_rating = self.average_rating * self.count_of_ratings
        new_total_rating = total_rating + rating
        new_count = self.count_of_ratings + 1

        self.count_of_ratings = new_count
        self.average_rating = round(new_total_rating / new_count, 1)

    def can_serve(self, car: Car) -> bool:
        """
        Check if the station can serve a specific car.

        A car can be served if its current cleanliness is less than
        the station's cleaning power.

        Args:
            car: Car object to check

        Returns:
            True if car can be served, False otherwise
        """
        return car.clean_mark < self.clean_power
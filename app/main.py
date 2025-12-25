from typing import List


class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> (
            None):
        """Initialize the Car with comfort class, clean mark, and brand."""
        self.comfort_class: int = comfort_class
        self.clean_mark: int = clean_mark
        self.brand: str = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        """Initialize the CarWashStation with its parameters."""
        self.distance_from_city_center: float = distance_from_city_center
        self.clean_power: int = clean_power
        self.average_rating: float = average_rating
        self.count_of_ratings: int = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculate the washing price for a given car.

        Price = (comfort_class * (clean_power - clean_mark) * rating)/distance
        """
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        Wash the given car if its clean mark is below the station's clean power
        After washing the car's clean mark will equal the station's clean power
        """
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: List[Car]) -> float:
        """
        Serve a list of cars, washing only those whose clean mark is below
        the station's clean power. Return the total income from washing.
        """
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, new_rating: float) -> None:
        """
        Add a new rating to the station, updating the average rating and
        the number of ratings.
        """
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)

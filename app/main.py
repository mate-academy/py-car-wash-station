from typing import List


class Car:
    """
    Represents a car with its comfort class, cleanness mark, and brand.
    """
    def __init__(
        self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    """
    Represents a car wash station and handles serving cars, calculating prices,
    and managing ratings.
    """
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        # Fix 1: Round the average_rating on assignment.
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        """
        Washes a list of cars if they are dirty enough and returns
        the total income.
        """
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculates the washing price for a single car based on a formula.
        """
        # Fix 2: Reformat the long expression to follow style guides.
        price = (car.comfort_class
                 * (self.clean_power - car.clean_mark)
                 * self.average_rating
                 / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        Updates a car's clean_mark to the station's clean_power.
        """
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rate: int) -> None:
        """
        Adds a new rating and recalculates the average rating.
        """
        current_total_rating = (
            self.average_rating * self.count_of_ratings
        )
        new_total_rating = current_total_rating + new_rate
        self.count_of_ratings += 1
        self.average_rating = round(
            new_total_rating / self.count_of_ratings, 1
        )
        

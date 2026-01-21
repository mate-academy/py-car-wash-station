from typing import List


class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        """Initialize Car instance."""
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        """Initialize CarWashStation instance."""
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        """Serve a list of cars and return the total income."""
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                wash_cost = self.calculate_washing_price(car)
                total_income += wash_cost
                self.wash_single_car(car)
        return total_income

    def calculate_washing_price(self, car: Car) -> float:
        """Calculate the washing price for a car."""
        return round(car.comfort_class
                     * (self.clean_power - car.clean_mark)
                     * self.average_rating
                     / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> None:
        """Wash a single car if its clean_mark is below clean_power."""
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        """Rate the service of the car wash station."""
        total_ratings = self.average_rating * self.count_of_ratings
        total_ratings += rating
        self.count_of_ratings += 1
        self.average_rating = round(total_ratings / self.count_of_ratings, 1)

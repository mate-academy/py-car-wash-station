from typing import List


class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        """
        :param comfort_class: Comfort class of the car (1-7)
        :param clean_mark: Cleanliness level of the car (1-10)
        :param brand: Brand of the car
        """
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        """
        :param distance_from_city_center: Distance from city center (1.0–10.0)
        :param clean_power: Max clean mark this station can achieve
        :param average_rating: Current average rating (1.0–5.0)
        :param count_of_ratings: Number of ratings received
        """
        if not (1.0 <= distance_from_city_center <= 10.0):
            raise ValueError("Distance from city center must be between 1.0 and 10.0")

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculates price for washing one car.
        """
        if car.clean_mark >= self.clean_power:
            return 0.0
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        Washes the car to station's clean power if applicable.
        """
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: List[Car]) -> float:
        """
        Washes all cars that qualify. Returns total income.
        """
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, new_rating: int) -> None:
        """
        Updates rating statistics with a new customer rating.
        """
        total_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        total_rating += new_rating
        self.average_rating = round(total_rating / self.count_of_ratings, 1)

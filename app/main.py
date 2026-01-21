from typing import List


class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
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
        """
        Calculates the washing price for a single car
        based on its cleanliness and the station's parameters.
        The result is rounded to 1 decimal.

        :param car: instance of class Car
        :return: float - calculated price for washing the car
        """
        calculate_price = round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center,
            1,
        )
        return calculate_price

    def wash_single_car(self, car: Car) -> None:
        """
        Washes a single car if its current cleanliness level is below
        the station's clean_power. Updates car.clean_mark to clean_power.

        :param car: instance of class Car
        :return: None
        """
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def calculate_washing_income(self, cars_to_clean: List[Car]) -> float:
        """
        Calculates the total washing income for a group of cars that require
        cleaning. Each car's washing price is computed and the result is
        rounded to 1 decimal.

        :param cars_to_clean: list of Car instances
        :return: float - car wash station income for serve List[Car],
        rounded to 1 decimal
        """
        income = round(
            sum(self.calculate_washing_price(car) for car in cars_to_clean), 1
        )
        return income

    def wash_group_of_cars(self, cars_to_clean: List[Car]) -> None:
        """
        Washes a group of cars by applying wash_single_car to each one.
        This method updates the cleanliness level of all cars
        that require washing.

        :param cars_to_clean: list of Car instances
        :return: None
        """
        for car in cars_to_clean:
            self.wash_single_car(car)

    def serve_cars(self, cars: List[Car]) -> float:
        """
        Serves a list of cars by selecting those that require washing,
        calculating the total washing income for them, and then washing
        each selected car. The total income is returned.

        :param cars: list of Car instances to be processed
        :return: float - total income from washing eligible cars
        """
        cars_to_clean = [
            car for car in cars
            if car.clean_mark < self.clean_power
        ]
        income = self.calculate_washing_income(cars_to_clean)
        self.wash_group_of_cars(cars_to_clean)

        return income

    def rate_service(self, new_rate: int) -> None:
        """
        Adds a new rating to the wash station and updates the average rating
        based on all received ratings.
        Also increases the total count of ratings.

        :param new_rate: integer rating value given by a customer
        :return: None
        """
        recalculated_avg_rating = round(
            (self.average_rating * self.count_of_ratings + new_rate)
            / (self.count_of_ratings + 1),
            1,
        )

        self.average_rating = recalculated_avg_rating
        self.count_of_ratings += 1

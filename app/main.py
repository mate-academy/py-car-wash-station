from typing import Callable


def limiter(
        value: float | int,
        type_func: Callable,
        limits: tuple[float | int, float | int]
) -> float | int:
    """
    Clamps a value and casts it to a specified type

    Args:
    value (float | int): The value to be clamped
    type_func (Callable): Type function, e.g., int or float
    limits: (tuple[float | int, float | int ]): Allowed limits

    Returns:
    float | int: The clamped value with the specified type
    """
    return min(max(type_func(value), limits[0]), limits[1])


class Car:
    """
    Represents a car

    Attributes:
    comfort_class (int): Comfort level of the car (1–7)
    clean_mark (int): Cleanliness level of the car (1–10)
    brand (str): Brand of the car
    """
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        """
        Initializes a Car instance

        Args:
        comfort_class (int): Comfort level of the car (1–7)
        clean_mark (int): Cleanliness level of the car (1–10)
        brand (str): Brand of the car
        """
        self.comfort_class = limiter(comfort_class, int, (1, 7))
        self.clean_mark = limiter(clean_mark, int, (1, 10))
        self.brand = str(brand)


class CarWashStation:
    """
    Represents a car wash station

    Attributes:
    distance_from_city_center (float): Distance to city center (1.0–10.0)
    clean_power (int): Maximum cleanliness level the station can achieve
    average_rating (float): Average rating of the station (1.0–5.0)
    count_of_ratings (int): Number of ratings the station has received
    """
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        """
        Initializes a CarWashStation instance

        Args:
        distance_from_city_center(float): Distance to city center (1.0–10.0)
        clean_power(int): Maximum cleanliness level the station can achieve
        average_rating(float): Average rating of the station (1.0–5.0)
        count_of_ratings(int): Number of ratings the station has received
        """
        self.distance_from_city_center = limiter(
            distance_from_city_center, float, (1.0, 10.0)
        )
        self.clean_power = limiter(
            clean_power, int, (1, 10)
        )
        self.average_rating = round(limiter(
            average_rating, float, (1.0, 5.0)
        ), 1)
        self.count_of_ratings = int(count_of_ratings)

    def serve_cars(self, cars: list[Car]) -> float:
        """
        Serves a list of cars,
        washing only those with clean_mark < clean_power

        Args:
        cars (list[Car]): List of cars to serve

        Returns:
        float: Income from serving these cars, rounded to 1 decimal
        """
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculates the cost of washing a single car

        Args:
        car (Car): The car to calculate the washing price for

        Returns:
        float: Cost of washing, rounded to 1 decimal
        """
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center,
            1
        )

    def wash_single_car(self, car: Car) -> None:
        """
        Washes a single car if its clean_mark
        is less than the station's clean_power

        Args:
        car (Car): The car to wash
        """
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        """
        Adds a new rating to the station
        and updates average_rating and count_of_ratings

        Args:
        rate (float): The rating to add (1.0–5.0)
        """
        self.count_of_ratings += 1
        self.average_rating = round(
            self.average_rating
            + (limiter(rate, float, (1.0, 5.0)) - self.average_rating)
            / self.count_of_ratings,
            1
        )

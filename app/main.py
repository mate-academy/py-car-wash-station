class Car:
    """
    Represents a car with comfort class, cleanliness mark and brand.

    Attributes:
        comfort_class (int): Comfort class from 1 to 7.
        clean_mark (int): Cleanliness mark from 1 to 10.
        brand (str): Brand of the car.
    """

    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str
    ) -> None:
        """
        Initializes a Car instance.

        Args:
            comfort_class (int): Comfort class from 1 to 7.
            clean_mark (int): Cleanliness mark from 1 to 10.
            brand (str): Brand of the car.

        Raises:
            ValueError: If any argument is out of valid range.
        """
        if not 1 <= comfort_class <= 7:
            raise ValueError("comfort_class must be between 1 and 7")
        if not 1 <= clean_mark <= 10:
            raise ValueError("clean_mark must be between 1 and 10")
        if not isinstance(brand, str) or not brand.strip():
            raise ValueError("brand must be a non-empty string")
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    """
    Represents a car wash station with attributes and methods to serve cars.

    Attributes:
        distance_from_city_center (float): (1.0 to 10.0).
        clean_power (int): Clean power of the station (1 to 10).
        average_rating (float): Average rating of the station (1.0 to 5.0).
        count_of_ratings (int): (equal to or greater than 0).
    """

    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        """
        Initializes a CarWashStation instance.

        Args:
            distance_from_city_center (float): (1.0 to 10.0).
            clean_power (int): Clean power of the station (1 to 10).
            average_rating (float): Average rating of the station (1.0 to 5.0).
            count_of_ratings (int): (equal to or greater than 0).

        Raises:
            ValueError: If any argument is out of valid range.
        """

        if not 1.0 <= distance_from_city_center <= 10.0:
            raise ValueError(
                "distance_from_city_center must be between 1.0 and 10.0"
            )
        if not 1 <= clean_power <= 10:
            raise ValueError(
                "clean_power must be between 1 and 10"
            )
        if not 1.0 <= average_rating <= 5.0:
            raise ValueError(
                "average_rating must be between 1.0 and 5.0"
            )
        if not 0 <= count_of_ratings:
            raise ValueError(
                "count_of_ratings must be equal to or greater than 0"
            )

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: list) -> float:
        """
        Serves a list of cars, washing those with clean_mark < clean_power and
        return income rounded to 1 decimal.

        Args:
            list_of_cars (list): List of Car instances to be served.

        Returns:
            float: The income of the car wash station for serving the list of
            cars.
        """

        income = 0.0
        for car in list_of_cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculates the cost for washing a single car based on the formula
        washing_price = (comfort_class * (clean_power - clean_mark)
                        * average_rating
                        / distance_from_city_center).

        Returns:
            float: The calculated washing price, rounded to 1 decimal.
        """
        return round((car.comfort_class
                     * (self.clean_power - car.clean_mark)
                     * self.average_rating
                     / self.distance_from_city_center), 1)

    def wash_single_car(self, car: Car) -> None:
        """
        Washes a single car by setting its clean_mark to clean_power if
        clean_mark is less than clean_power.

        Args:
            car (Car): The car to be washed.
        """
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
        return None

    def rate_service(self, rating: float) -> None:
        """
        Adds a single rating to the wash station and updates average_rating
        and count_of_ratings accordingly.

        Args:
            rating (float): The rating to be added (1.0 to 5.0).

            Raises:
                ValueError: If the rating is not between 1.0 and 5.0.
        """
        if not 1.0 <= rating <= 5.0:
            raise ValueError("rating must be between 1.0 and 5.0")
        self.average_rating = round((self.average_rating
                                    * self.count_of_ratings + rating)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

"""Contains Car and CarWashStation classes."""


class Car:
    """Class implementation for a car."""

    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str
    ) -> None:
        """Create an instance of a car.

        Args:
            comfort_class - car comfort class from 1 to 7
            clean_mark - car cleanness level from 1 to 10
            brand - car brand name

        Returns:
            An instance of a Car class
        """
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    """Class implementation for a car wash station."""

    def __init__(
        self,
        distance_from_city_center: int,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        """Create an instance of a car wash station.

        Args:
            distance_from_city_center - distance from city center from 1 to 10
            clean_power - the level of cleanness the station provides
            averate_rating - average ratinf of the station from 1.0 to 5.0
            count_of_ratings - total amount of the station ratings

        Returns:
            An instalce of a CarWashStation class
        """
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        """Service list of cars and return total income of service.

        Args:
            cars: - list of Car class instances

        Returns:
            Total amount of service cost
        """
        total_income = 0

        for car in cars:
            if self.is_serviceable(car):
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return total_income

    def calculate_washing_price(self, car: Car) -> float:
        """Calculate service cost for a single car.

        Args:
            car - an instance of Car class

        Returns:
            Service cost for a single car
        """
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
            , 1
        )

    def wash_single_car(self, car: Car) -> None:
        """Update cleanness level for a single car.

        Args:
            car - an instance of Car class
        """
        car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        """Update average rating and total number of ratings.

        Args:
            rating - rating from 1 to 5
        """
        current_total_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round(
            (current_total_rating + rating)
            / self.count_of_ratings
            , 1
        )

    def is_serviceable(self, car: Car) -> bool:
        """Check if a car could be serviceable.

        Args:
            car - an instance of Car class

        Returns:
            A result of a car check for the service
        """
        return car.clean_mark < self.clean_power

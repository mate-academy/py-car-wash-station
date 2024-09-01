class Car:
    """
    A class representing a car.

    Attributes:
        comfort_class (int): The comfort class of the car.
        clean_mark (int): The cleanliness level of the car, on a scale from 0 to 10.
        brand (str): The brand of the car.
    """

    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        """
        Initializes a Car object.

        Args:
            comfort_class (int): The comfort class of the car.
            clean_mark (int): The cleanliness level of the car.
            brand (str): The brand of the car.
        """
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    """
    A class representing a car wash station.

    Attributes:
        distance_from_city_center (float): Distance of the car wash from the city center.
        clean_power (int): Cleaning power of the car wash station.
        average_rating (float): Average rating of the car wash station.
        count_of_ratings (int): Total number of ratings received.
    """

    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        """
        Initializes a CarWashStation object.

        Args:
            distance_from_city_center (float): Distance of the car wash from the city center.
            clean_power (int): Cleaning power of the car wash station.
            average_rating (float): Average rating of the car wash station.
            count_of_ratings (int): Total number of ratings received.
        """
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        """
        Washes all cars that need cleaning and calculates total income.

        Args:
            cars (list[Car]): List of Car objects to be washed.

        Returns:
            float: Total income generated from washing the cars rounded to 1 decimal.
        """
        cars_for_wash = filter(lambda car: car.clean_mark < self.clean_power, cars)
        income = 0
        for car in cars_for_wash:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)

        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculates the price for washing a single car.

        Args:
            car (Car): The car to be washed.

        Returns:
            float: The calculated price for washing the car rounded to 1 decimal.
        """
        clean_difference = (self.clean_power - car.clean_mark)
        gen_price = car.comfort_class * clean_difference * self.average_rating
        price = gen_price / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        Washes a single car, improving its clean_mark to the station's clean_power.

        Args:
            car (Car): The car to be washed.
        """
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        """
        Rates the car wash service and updates the average rating.

        Args:
            rate (int): The rating provided by a customer.
        """
        total_rate = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(total_rate / self.count_of_ratings, 1)

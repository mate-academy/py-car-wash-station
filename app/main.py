class Car:
    """
    Represents a car with its comfort class, cleanliness level, and brand.

    A `Car` instance holds information about its comfort classification,
    cleanliness rating, and brand name. This information can be utilized
    for various purposes, including evaluation, comparison, and
    categorization of cars.

    """

    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:
        """
        Represents a vehicle with defined comfort class, cleanliness level,
        and brand.

        The class serves as a basic representation of a vehicle that can be
        associated with certain attributes such as the level of comfort it
        provides, its cleanliness rating, and the brand it is manufactured
        from.

        :param comfort_class: Integer representing the comfort classification
                              of the vehicle.
        :type comfort_class: int
        :param clean_mark: Integer denoting the cleanliness level of the
                           vehicle.
        :type clean_mark: int
        :param brand: The brand name of the vehicle as a string.
        :type brand: str
        """
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    """
    A class representing a car wash station with capabilities
    to serve cars, calculate washing price, and manage ratings.

    This class manages the functionality of a car wash station,
    including serving cars based on their cleanliness,
    calculating prices of washing services, performing the washing
    operation, and allowing users to rate the service.
    The cleaning efficiency depends on various station and car
    attributes such as cleaning power, rating of the station, and the
    comfort class of the car.

    """

    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: float
                 ) -> None:
        """
        Class representing a specific data model with attributes for
        tracking various metrics.

        :param distance_from_city_center: Distance from the city
        center in a specific unit.
        :type distance_from_city_center: float
        :param clean_power: Level or percentage of clean power usage.
        :type clean_power: int
        :param average_rating: Average rating score from user reviews.
        :type average_rating: float
        :param count_of_ratings: Total count of ratings used to
        determine the average.
        :type count_of_ratings: int
        """
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        """
        Washes and calculates the total income from a list of cars.

        Each car in the list is checked to see if its cleanliness level is
        below the washing threshold (clean_power). If so, the car is washed,
        and the price for washing is added to the total income, which is
        returned rounded to one decimal place.

        :param cars: List of Car objects to be processed.
        :type cars: list[Car]
        :return: The total income generated from washing the cars.
        :rtype: float
        """
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                total_income += price
                self.wash_single_car(car)
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculate the washing price for a given car.

        This method calculates the price for washing a car based
        on various factors such as the car's comfort class,
        cleanliness rating, the cleaning power of the service,
        the average rating of the provider, and the distance of
        the car wash service from the city center. The resulting price
        is rounded to one decimal place.

        :param car: The car object for which the washing price needs to
            be calculated.
        :type car: Car
        :return: The calculated washing price as a floating-point number.
        :rtype: float
        """
        comfort_cost = car.comfort_class
        clean_difference = self.clean_power - car.clean_mark
        rating_factor = self.average_rating
        distance_factor = self.distance_from_city_center

        base_price = comfort_cost * clean_difference

        rated_price = base_price * rating_factor

        price = rated_price / distance_factor

        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        Washes a single car by increasing its cleanliness
        level based on the washing machine's cleaning power.

        :param car: The car object to be washed.
        :type car: Car
        :return: None
        """
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rating: float) -> None:
        """
        Updates the average rating of a service based on a new rating
        provided. It adjusts the total rating by incorporating the new rating,
        increments the count of ratings, and calculates the updated average
        rating rounded to one decimal place.

        :param new_rating: The new rating to incorporate into the
        average (float).
        :return: None
        """
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)

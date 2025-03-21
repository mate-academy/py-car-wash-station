class Car:
    """
    Represents a car with attributes for comfort, cleanliness, and brand.

    :param comfort_class: The comfort level of the car (higher is better).
    :type comfort_class: int
    :param clean_mark: The cleanliness rating of the car (higher is cleaner).
    :type clean_mark: int
    :param brand: The brand of the car.
    :type brand: str
    """

    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    """
    Represents a car wash station with attributes for its location,
    cleaning capability, and customer ratings.

    :param distance_from_city_center: Distance of the car wash
        from the city center.
    :type distance_from_city_center: float
    :param clean_power: The cleaning effectiveness of the car wash.
    :type clean_power: int
    :param average_rating: The current average rating of the car wash.
    :type average_rating: float
    :param count_of_ratings: The total number of ratings received.
    :type count_of_ratings: int
    """

    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        """
        Washes a list of cars and calculates the total income.

        :param cars: A list of cars to be washed.
        :type cars: list[Car]
        :return: The total income generated from washing cars.
        :rtype: float
        """
        income = 0
        for car in cars:
            if self._is_car_wash_possible(car):
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculates the washing price for a given car.

        :param car: The car to calculate the washing price for.
        :type car: Car
        :return: The price of washing the car.
        :rtype: float
        """
        return round(car.comfort_class * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        Washes a single car by updating its clean mark.

        :param car: The car to be washed.
        :type car: Car
        """
        if self._is_car_wash_possible(car):
            car.clean_mark = self.clean_power

    def rate_service(self, new_rate: int) -> None:
        """
        Updates the average rating of the car wash station
        based on a new rating and increase rating counter by 1.
        :param new_rate: The new rating given by a customer.
        :type new_rate: int
        """
        self.average_rating = self._recalculate_rating(new_rate)
        self.count_of_ratings += 1

    def _is_car_wash_possible(self, car: Car) -> bool:
        """
        Checks if the car wash can improve the clean mark of the given car.

        :param car: The car to check.
        :type car: Car
        :return: True if the car wash is possible, False otherwise.
        :rtype: bool
        """
        if self.clean_power > car.clean_mark:
            return True
        return False

    def _recalculate_rating(self, new_rate: int) -> float:
        """
        Recalculates the average rating based on a new customer rating.

        :param new_rate: The new rating to incorporate.
        :type new_rate: int
        :return: The updated average rating.
        :rtype: float
        """
        result = self.average_rating * self.count_of_ratings
        result += new_rate
        result /= self.count_of_ratings + 1
        return round(result, 1)

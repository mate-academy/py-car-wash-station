class Car:
    """
    :param comfort_class: comfort class of a car, from 1 to 7
    :param clean_mark: car cleanness mark, from very dirty to clean
    :param brand: brand of the car
    """
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
    """
    :param distance_from_city_center: how far station from the city center
    :param clean_power: clean_mark to which this car wash station washes
    :param average_rating: average rating of the station
    :param count_of_ratings: number of people who rated
    """
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int, average_rating: float
            , count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, client_cars: list) -> float:
        """
        method, that takes a list of Car's, washes only cars with
        clean_mark < clean_power of wash station

        :param client_cars: income of CarWashStation for serving list of Car's
        :return: returns income rounded to 1 decimal
        """
        income = 0
        washed_cars = [
            car for car in client_cars
            if car.clean_mark < self.clean_power
        ]
        for car in washed_cars:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        """
        method, that calculates cost for a single car wash

        :param car: a car that we need to calculate the price for
        :return: returns number rounded to 1 decimal
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
        method, that washes a single car

        :param car: single washed car
        :return: new clean_mark of a car
        """
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        """
        method that adds a single rate to the wash station

        :param rate: rate from client
        :return: average_rating and count_of_ratings
        """
        self.count_of_ratings += 1
        new_rating = ((self.average_rating
                       * (self.count_of_ratings - 1)
                       + rate)
                      / self.count_of_ratings)

        self.average_rating = round(new_rating, 1)

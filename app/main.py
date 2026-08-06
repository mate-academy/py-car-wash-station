from typing import List


class Car:
    def __init__(self, comfort_class: float,
                 clean_mark: float, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: float,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        """
        method, that takes a list of Car's,
        washes only cars with clean_mark < clean_power of wash station
        and returns income of CarWashStation for serving this list of Car's,
        rounded to 1 decimal

        @:param cars: list of Car's
        @:return income: float
        """

        income = 0.0
        for car in cars:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        """
        method, that calculates cost for a single car wash,
        cost is calculated as: car's comfort class * difference
        between wash station's clean power and car's clean mark
        * car wash station rating / car wash station distance to the center
        of the city, returns number rounded to 1 decimal

        :param car: Car
        :return: float
        """
        price = (((car.comfort_class * (self.clean_power - car.clean_mark))
                  * self.average_rating) / self.distance_from_city_center)

        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        method, that washes a single car, so it should have clean_mark
        equals wash station's clean_power, if wash_station.clean_power
        is greater than car.clean_mark

        :param car: Car
        :return: None
        """
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        """
        method, that calculates cost for a single car wash,
        cost is calculated as: car's comfort class * difference
        between wash station's clean power and
        car's clean mark * car wash station rating / car wash station distance
        to the center of the city, returns number rounded to 1 decimal

        :param rating: float
        :return: None
        """
        self.average_rating = round((self.average_rating
                                     * self.count_of_ratings + rating)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

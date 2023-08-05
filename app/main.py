class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: int,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        """
        Method, that takes a list of Car's,
        washes only cars with clean_mark < clean_power of wash station.

        :param cars: a list of cars we need to serve
        :return: returns income of CarWashStation
        for serving this list of Car's,
        rounded to 1 decimal
        """
        income = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        """
        Method, that calculates cost for a single car wash

        :param car: a car that we need to calculate the price for
        :return: returns number rounded to 1 decimal
        """
        power_mark_difference = self.clean_power - car.clean_mark
        washing_price = (car.comfort_class
                         * power_mark_difference
                         * self.average_rating
                         / self.distance_from_city_center)
        return round(washing_price, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        Method, that washes a single car

        :param car: a car that we want to wash
        :return: it should have clean_mark equals wash station's clean_power,
        if wash_station.clean_power is greater than car.clean_mark
        """
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        """
        Method that adds a single rate to the wash station

        :param rating: rating that we want to add
        :return: based on this single rate average_rating
        and count_of_ratings should be changed
        """
        new_average = round(
            (self.count_of_ratings * self.average_rating + rating)
            / (self.count_of_ratings + 1),
            1)
        self.count_of_ratings += 1
        self.average_rating = new_average

class Car:
    """
    Class Car, its __init__ method takes and stores 3 arguments:

    comfort_class - comfort class of a car, from 1 to 7
    clean_mark - car cleanness mark, from very dirty - 1 to absolutely
    clean - 10 brand - brand of the car
    """
    def __init__(
            self,
            comfort_class: float,
            clean_mark: float,
            brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    """
    Class CarWashStation, its __init__ method takes and stores 4 arguments:

    distance_from_city_center - how far station from the city center,
    from 1.0 to 10.0 clean_power - clean_mark to which this car wash
    station washes (yes, not all stations can clean your car completely)
    average_rating - average rating of the station, from 1.0 to 5.0, rounded
    to 1 decimal count_of_ratings - number of people who rated
    """
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: float,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: list[Car]) -> float:
        """
        serve_cars - method, that takes a list of Car's, washes only cars
        with clean_mark < clean_power of wash station and returns income
        of CarWashStation for serving this list of Car's, rounded to 1 decimal:
        """
        income = 0
        for car in list_of_cars:
            if car.clean_mark < self.clean_power:
                income += round(self.calculate_washing_price(car), 1)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        """
        calculate_washing_price - method, that calculates cost for a single car
        wash, cost is calculated as: car's comfort class * difference between
        wash station's clean power and car's clean mark * car wash station
        rating / car wash station distance to the center of the city, returns
        number rounded to 1 decimal.
        """
        return round(car.comfort_class
                     * (self.clean_power - car.clean_mark)
                     * self.average_rating
                     / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        wash_single_car - method, that washes a single car, so it should have
        clean_mark equals wash station's clean_power, if
        wash_station.clean_power is greater than car.clean_mark.
        """
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate_index: int) -> None:
        """
        rate_service - method that adds a single rate to the wash station,
        and based on this single rate average_rating and count_of_ratings
        should be changed.
        """
        self.average_rating = round(
            ((self.average_rating * self.count_of_ratings) + rate_index)
            / (self.count_of_ratings + 1), 1
        )
        self.count_of_ratings += 1

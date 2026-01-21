class Car:
    """
    comfort_class - comfort class of a car, from 1 to 7
    clean_mark - car cleanness mark,
    from very dirty - 1 to absolutely clean - 10
    brand - brand of the car
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
    distance_from_city_center
        - how far station from the city center, from 1.0 to 10.0
    clean_power - clean_mark to which this car wash station washes
    average_rating - average rating of the station,
        from 1.0 to 5.0, rounded to 1 decimal
    count_of_ratings - number of people who rated
    """
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        """
        washes only cars with clean_mark < clean_power of wash station
        returns income of CarWashStation for serving this list of Car's,
        rounded to 1 decimal
        """
        car_wash_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                car_wash_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(car_wash_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        """
        calculates cost for a single car wash, cost is calculated as:
        car's comfort class *
        difference between wash station's clean power and car's clean mark *
        car wash station rating /
        car wash station distance to the center of the city;
        returns number rounded to 1 decimal
        """
        difference = self.clean_power - car.clean_mark
        multiplication = car.comfort_class * difference * self.average_rating
        return round(multiplication / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        should have clean_mark equals wash station's clean_power,
        if wash_station.clean_power is greater than car.clean_mark
        """
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        """
        adds a single rate to the wash station
        """
        rate_sum = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round(
            (rate_sum + rate) / self.count_of_ratings, 1
        )

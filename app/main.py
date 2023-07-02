class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
        sum_of_ratings: int = 0,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
        self.sum_of_ratings = average_rating * count_of_ratings

    def calculate_washing_price(self, car: str) -> float:
        """
        method, that calculates
        cost for a single car wash, cost is calculated as:
        car's comfort class * difference between wash station's
        clean power and car's clean mark * car wash station rating
        / car wash station distance to the center of the city,
        returns number rounded to 1 decimal;
        """

        return round(
            car.comfort_class
            * abs(self.clean_power - car.clean_mark)
            * (self.average_rating / self.distance_from_city_center),
            1,
        )

    def serve_cars(self, cars: list[str]) -> float:
        """
        method, that takes a list of Car's, washes only
        cars with clean_mark < clean_power of wash station
        and returns income of CarWashStation for serving
        this list of Car's, rounded to 1 decimal.
        """

        result = 0

        for car in cars:
            if self.clean_power > car.clean_mark:
                result += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(result, 1)

    def wash_single_car(self, car: str) -> None:
        """
        method, that washes a single car,
        so it should have clean_mark equals
        wash station's clean_power, if
        wash_station.clean_power is greater
        than car.clean_mark;
        """
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, service_mark: int) -> None:
        """
        method that adds a single rate to the wash station,
        and based on this single rate average_rating and
        count_of_ratings should be changed
        """

        self.sum_of_ratings += service_mark
        self.count_of_ratings += 1
        self.average_rating = round(
            self.sum_of_ratings / self.count_of_ratings, 1
        )

class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    cars_ = []

    def __init__(
        self,
        distance_from_city_center: int,
        clean_power: int,
        average_rating: int,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: list) -> float:
        """1. `serve_cars` - method, that takes a list of `Car`'s, washes only
        cars with `clean_mark` < `clean_power` of wash station
        and returns income of `CarWashStation` for serving this list of Car's,
        rounded to 1 decimal:"""
        res = []
        for car in car_list:
            if car.clean_mark <= self.clean_power:
                res.append(self.wash_single_car(car))
                car.clean_mark = self.clean_power
        return sum(res)

    def calculate_washing_price(self, car: Car) -> float:
        """2. `calculate_washing_price` - method, that calculates cost for a
        single car wash,
        cost is calculated as: car's comfort class * difference between
        wash station's clean power and car's clean mark * car wash station
        rating / car wash station
        distance to the center of the city, returns number rounded
        to 1 decimal;"""
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center,
            1,
        )

    def wash_single_car(self, car: Car) -> float:
        """wash_single_car - method, that washes a single car, so it should have clean_mark equals wash station's
        clean_power, if wash_station.clean_power is greater than car.clean_mark;"""
        if car.clean_mark <= self.clean_power:
            return round(self.calculate_washing_price(car), 1)

    def rate_service(self, a) -> None:
        """4. `rate_service` - method that adds a single rate to the wash station, and based on this single rate
        `average_rating` and `count_of_ratings` should be changed:"""
        self.average_rating = round(
            (a + self.count_of_ratings * self.average_rating)
            / (self.count_of_ratings + 1),
            1,
        )
        self.count_of_ratings = self.count_of_ratings + 1

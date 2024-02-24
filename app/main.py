class Car:
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
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def check_car(self, car: Car) -> bool:
        """Method checks, if Car can be cleaned by CarWashStation"""
        return car.clean_mark < self.clean_power

    def calculate_washing_price(self, car: Car) -> int:
        """
        Method, that calculates cost for a single car wash rounded to 1 decimal
        """
        if not self.check_car(car):
            return 0
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center,
            1,
        )

    def wash_single_car(self, car: Car) -> None:
        """
        Method, that washes a single car
        """
        if self.check_car(car):
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        """method that adds a single rate to the wash station,
        and cahange average_rating and count_of_ratings
        """
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rate)
            / (self.count_of_ratings + 1),
            1,
        )
        self.count_of_ratings += 1

    def serve_cars(self, cars: list[Car]) -> float:
        """
        Method, that takes a list of Car's,
        washes only cars with clean_mark < clean_power
        of wash station and returns income of CarWashStation
        for serving this list of Car's, rounded to 1 decimal
        """
        income = 0
        for car in cars:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return income

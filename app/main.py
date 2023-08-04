class CarValidationError(Exception):
    """There's error with initialization of
    Car object"""


class CarWashStationError(Exception):
    """There's error with initialization of
    CarWashStation object"""


class Car:
    def __init__(
            self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:
        if not 1 <= comfort_class <= 7:
            raise CarValidationError(
                f"Comfort class should be between 1 and 7,"
                f" actual value {comfort_class}"
            )

        if not 1 <= clean_mark <= 10:
            raise CarValidationError(
                f"Clean mark should be between 1 and 10,"
                f" actual value {comfort_class}"
            )

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        if not 1 <= distance_from_city_center <= 10:
            raise CarWashStationError(
                f"Distance should be between 1.0 and 10.0,"
                f" actual value {distance_from_city_center}"
            )
        if not 1 <= average_rating <= 5:
            raise CarWashStationError(
                f"Average rating should be between 1.0 and 5.0,"
                f" actual value {average_rating}"
            )
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def check_if_suitable(self, list_of_cars: list) -> list:
        return [
            car for car in list_of_cars if car.clean_mark < self.clean_power
        ]

    def serve_cars(self, list_of_cars: list) -> float:
        suitable_cars = self.check_if_suitable(list_of_cars)

        income = 0
        for car in suitable_cars:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)

        return income

    def calculate_washing_price(self, car: Car) -> float:
        cleaned_difference = self.clean_power - car.clean_mark
        station_rate = self.average_rating / self.distance_from_city_center
        income = round(
            car.comfort_class * cleaned_difference * station_rate, 1
        )

        return income

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, new_rating: int) -> None:
        total_score = self.average_rating * self.count_of_ratings
        total_score += new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_score / self.count_of_ratings, 1)

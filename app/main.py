def validate_func(
        value: float,
        min_value: float,
        max_value: float,
        name_argument: str
) -> int | float:
    if min_value <= value <= max_value:
        return value


class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class = validate_func(
            comfort_class,
            1,
            7,
            "comfort_class"
        )
        self.clean_mark = validate_func(
            clean_mark,
            1,
            10,
            "clean_mark"
        )
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:

        self.distance_from_city_center = validate_func(
            distance_from_city_center,
            1.0,
            10.0,
            "distance_from_city_center")
        self.clean_power = clean_power
        self.average_rating = round(
            validate_func(
                average_rating,
                1.0,
                5.0,
                "average_rating"
            ), 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: list) -> float:
        income = 0
        for car in list_of_cars:
            if car.clean_mark < self.clean_power:
                income += round(self.calculate_washing_price(car), 1)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        difference_cleaning = self.clean_power - car.clean_mark
        return (car.comfort_class
                * difference_cleaning
                * self.average_rating
                / self.distance_from_city_center)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        self.average_rating = round(
            (self.average_rating
             * self.count_of_ratings
             + rate)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

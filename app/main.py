class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        _check_value("comfort_class", comfort_class, 1, 7)
        _check_value("clean_mark", clean_mark, 1, 10)

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self, distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        _check_value(
            "distance_from_city_center",
            distance_from_city_center,
            1.0,
            10.0
        )
        _check_value("average_rating", average_rating, 1.0, 5.0)

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        cost = 0

        for car in cars:
            if self.clean_power > car.clean_mark:
                cost += self.calculate_washing_price(car)
                self.wash_single_car(car)
                print(cost)

        return cost

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * (self.average_rating / self.distance_from_city_center),
            1
        )

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rate)
            / (self.count_of_ratings + 1),
            1
        )
        self.count_of_ratings += 1


def _check_value(
        value_name: str,
        value: int | float,
        lower_limit: int | float,
        upper_limit: int | float
) -> None:
    if not (lower_limit <= value <= upper_limit):
        raise ValueError(
            f"{value_name} must be between {lower_limit} and {upper_limit}"
        )

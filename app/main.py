from decimal import ROUND_HALF_UP, Decimal


def _round1(value: float) -> float:
    """Round to 1 decimal place, rounding half up."""
    exact_value = Decimal(str(round(value, 9)))
    rounded = exact_value.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
    return float(rounded)


class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str,
    ) -> None:
        # comfort_class: 1..7, clean_mark: 1..10
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
        # distance: 1.0..10.0, average_rating: 1.0..5.0
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return _round1(price)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return _round1(income)

    def rate_service(self, rate: float) -> None:
        total = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = _round1(total / self.count_of_ratings)

from decimal import Decimal, ROUND_HALF_UP

class Car:
    def __init__(
            self, comfort_class: int,
            clean_mark: int,
            brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        result = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                result += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(result, 1)

    def calculate_washing_price(self, car: Car) -> float:
        raw = (
            Decimal(str(car.comfort_class)) *
            (Decimal(str(self.clean_power)) - Decimal(str(car.clean_mark))) *
            Decimal(str(self.average_rating)) /
            Decimal(str(self.distance_from_city_center))
        )
        return float(raw.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        total = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = (
            round((total + rate) / self.count_of_ratings, 1))

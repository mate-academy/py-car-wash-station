from decimal import Decimal, ROUND_HALF_UP


class Car:
    def __init__(
        self, comfort_class: int, clean_mark: int, brand: str
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

    def calculate_washing_price(self, car: Car) -> float:
        rating = Decimal(str(self.average_rating))
        distance = Decimal(str(self.distance_from_city_center))
        power_diff = Decimal(self.clean_power) - Decimal(car.clean_mark)
        price = Decimal(car.comfort_class) * power_diff * rating / distance
        return float(
            price.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        )

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> float:
        total_income = Decimal("0")
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = Decimal(str(self.calculate_washing_price(car)))
                total_income += price
                self.wash_single_car(car)
        return float(
            total_income.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        )

    def rate_service(self, rating: float) -> None:
        total = self.average_rating * self.count_of_ratings + rating
        self.count_of_ratings += 1
        new_average = Decimal(str(total)) / Decimal(str(self.count_of_ratings))
        self.average_rating = float(
            new_average.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        )

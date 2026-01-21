from decimal import Decimal, ROUND_HALF_UP

def round_half_up(value: float, ndigits: int = 1) -> float:
    return float(Decimal(str(value)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))

class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int | float,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round_half_up(average_rating)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: "Car") -> float:
        delta = max(self.clean_power - car.clean_mark, 0)
        price = car.comfort_class * delta * self.average_rating / self.distance_from_city_center
        return round_half_up(price)

    def wash_single_car(self, car: "Car") -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list["Car"]) -> float:
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round_half_up(total_income)

    def rate_service(self, rate: int | float) -> None:
        total_score = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round_half_up((total_score + rate) / self.count_of_ratings)
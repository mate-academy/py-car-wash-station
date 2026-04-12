def validate(meaning: str, value: float, min_val: float,
             max_val: float) -> None:
    if not (min_val <= value <= max_val):
        raise ValueError(f"{meaning} must be between {min_val} and {max_val}")


class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        validate("comfort_class", comfort_class, 1, 7)
        self.comfort_class = comfort_class
        validate("clean_mark", clean_mark, 1, 10)
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        validate("distance_from_city_center",
                 distance_from_city_center, 1.0, 10.0)
        self.distance_from_city_center = distance_from_city_center
        validate("clean_power", clean_power, 1, 10)
        self.clean_power = clean_power
        validate("average_rating", average_rating, 1.0, 5.0)
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class
                     * (self.clean_power - car.clean_mark)
                     * self.average_rating
                     / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rate)
            / (self.count_of_ratings + 1), 1
        )
        self.count_of_ratings += 1

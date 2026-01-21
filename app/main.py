class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str
    ) -> None:
        self.comfort_class = self.validate(comfort_class, 1, 7)
        self.clean_mark = self.validate(clean_mark, 1, 10)
        self.brand = brand

    def validate(self, value: int, minimal: int, maximal: int) -> int:
        if minimal <= value <= maximal:
            return value
        return minimal


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = self.validate_clean_power(clean_power)
        self.average_rating = self.validate_average_rating(average_rating)
        self.count_of_ratings = (self.validate_count_of_ratings
                                 (count_of_ratings))

    def validate_distance(self, distance_from_city_center: float) -> float:
        if 1.0 <= distance_from_city_center <= 10.0:
            return distance_from_city_center
        return 1.0

    def validate_clean_power(self, clean_power: int) -> int:
        if 1 <= clean_power <= 10:
            return clean_power
        return 1

    def validate_average_rating(self, average_rating: float) -> float:
        if 1.0 <= average_rating <= 5.0:
            return round(average_rating, 1)
        return 1.0

    def validate_count_of_ratings(self, count_of_ratings: int) -> int:
        if count_of_ratings >= 0:
            return count_of_ratings
        return 0

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center,
            1
        )

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rate)
            / (self.count_of_ratings + 1),
            1
        )
        self.count_of_ratings += 1

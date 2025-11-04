class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

    def __repr__(self) -> str:
        return (f"{self.brand}(comfort={self.comfort_class}, "
                f"clean={self.clean_mark})")


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int | float,
                 average_rating: float, count_of_ratings: int) -> None:
        if not (1.0 <= distance_from_city_center <= 10.0):
            raise ValueError("distance_from_city_center "
                             "must be between 1.0 and 10.0")
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        if not (1.0 <= average_rating <= 5.0):
            raise ValueError("average_rating must be between 1.0 and 5.0")
        self.average_rating = average_rating
        if not isinstance(count_of_ratings, int) or count_of_ratings < 0:
            raise ValueError("count_of_ratings must be a non-negative integer")
        self.count_of_ratings = count_of_ratings

    def __repr__(self) -> str:
        return (f"distance={self.distance_from_city_center}, "
                f"power={self.clean_power}, "
                f"rating={self.average_rating}, count={self.count_of_ratings}")

    def rate_service(self, rate: int | float) -> float:
        if not (1.0 <= rate <= 5.0):
            raise ValueError("rate must be between 1.0 and 5.0")
        current_counts = self.count_of_ratings

        self.average_rating = ((self.average_rating * current_counts + rate)
                               / (current_counts + 1))
        self.average_rating = round(self.average_rating, 1)
        self.count_of_ratings += 1

        return self.average_rating

    def wash_single_car(self, car: "Car") -> int:
        if self.clean_power > car.clean_mark:
            car.clean_mark = int(self.clean_power)

        return car.clean_mark

    def calculate_washing_price(self, car: "Car") -> float:
        diff = self.clean_power - car.clean_mark
        if diff <= 0:
            return 0.0
        price = ((car.comfort_class * diff * self.average_rating)
                 / self.distance_from_city_center)

        return round(price, 1)

    def serve_cars(self, cars: list["Car"]) -> float:
        income = 0

        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(income, 1)

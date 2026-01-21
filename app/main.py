class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str
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
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        skipped_cars = []

        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                income += price
                self.wash_single_car(car)
            else:
                skipped_cars.append(car)

        self.handle_skipped_cars(skipped_cars)

        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        valid_distance = self.validate_distance()

        if valid_distance is None:
            return 0

        cleaning_difficulty = self.clean_power - car.clean_mark
        price = (
            car.comfort_class * cleaning_difficulty * self.average_rating
        ) / valid_distance

        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, mark: int) -> None:
        self.count_of_ratings += 1
        self.average_rating = round(
            (self.average_rating * (self.count_of_ratings - 1) + mark)
            / self.count_of_ratings,
            1
        )

    @staticmethod
    def handle_skipped_cars(skipped_cars: list[Car]) -> None:
        if not skipped_cars:
            return

        car_brands = [car.brand for car in skipped_cars]
        car_brands_str = ", ".join(car_brands)
        print(f"These cars did not need washing: {car_brands_str}")

    def validate_distance(self) -> float | None:
        if self.distance_from_city_center == 0:
            print(
                "Warning: Invalid distance from city center (0). "
                "Cannot calculate price."
            )
            return None

        return self.distance_from_city_center

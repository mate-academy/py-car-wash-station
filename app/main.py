class Car:
    def __init__(
        self,
        comfort_class: float,
        clean_mark: float,
        brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: float,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            improvement = self.clean_power - car.clean_mark
            car.clean_mark = self.clean_power
            return improvement
        return 0.0

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0.0
        for car in cars:
            old_clean_mark = car.clean_mark
            self.wash_single_car(car)
            improvement = car.clean_mark - old_clean_mark
            if improvement > 0:
                income = round(
                    improvement * car.comfort_class * self.average_rating
                    / self.distance_from_city_center,
                    1
                )
                total_income += income
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            improvement = self.clean_power - car.clean_mark
            price = round(
                improvement * car.comfort_class * self.average_rating
                / self.distance_from_city_center, 1)
            return price
        return 0.0

    def rate_service(self, rate: int) -> None:
        avg_rate = self.average_rating
        count_of_rates = self.count_of_ratings
        new_avg_rate = round(
            (avg_rate * count_of_rates + rate) / (count_of_rates + 1),
            1
        )
        self.average_rating = new_avg_rate
        self.count_of_ratings = count_of_rates + 1

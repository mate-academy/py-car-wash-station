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
        serving_income = 0
        for car in cars:
            serving_income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return round(serving_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        if not self.is_sense_to_wash(car):
            return 0.0
        difference = self.clean_power - car.clean_mark
        return round(
            car.comfort_class * difference * self.average_rating
            / self.distance_from_city_center, 1
        )

    def wash_single_car(self, car: Car) -> None:
        if self.is_sense_to_wash(car):
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        total_mark_before = self.average_rating * self.count_of_ratings
        total_mark_now = total_mark_before + rate
        self.count_of_ratings += 1
        self.average_rating = round(total_mark_now / self.count_of_ratings, 1)

    def is_sense_to_wash(self, car: Car) -> bool:
        if self.clean_power > car.clean_mark:
            return True
        return False

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

    def can_be_cleaned(self, mark: int) -> bool:
        return mark > self.clean_mark

    def update_mark(self, mark: int) -> None:
        if self.can_be_cleaned:
            self.clean_mark = mark


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
        total = 0
        for car in cars:
            if car.can_be_cleaned(self.clean_power):
                total += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total, 1)

    def wash_single_car(self, car: Car) -> None:
        car.update_mark(self.clean_power)

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            (car.comfort_class * (self.clean_power - car.clean_mark)
             * self.average_rating / self.distance_from_city_center), 1)

    def rate_service(self, rate: float) -> None:
        self.average_rating = round(
            ((self.average_rating * self.count_of_ratings + rate)
             / (self.count_of_ratings + 1)), 1)
        self.count_of_ratings += 1

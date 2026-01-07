class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def _is_enough_power(self, car: Car) -> bool:
        return self.clean_power > car.clean_mark

    def calculate_washing_price(self, car: Car) -> float:
        if self.distance_from_city_center == 0:
            self.distance_from_city_center = 1
        price = (car.comfort_class
                 * (self.clean_power - car.clean_mark)
                 * (self.average_rating / self.distance_from_city_center))
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        self.average_rating = round(
            ((self.average_rating * self.count_of_ratings) + rating)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        for car in cars:
            if self._is_enough_power(car):
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

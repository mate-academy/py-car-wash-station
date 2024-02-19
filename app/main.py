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
            distance_from_city_center: int,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        return round(
                (self.average_rating * car.comfort_class * (self.clean_power - car.clean_mark))
                / self.distance_from_city_center,
                1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        self.count_of_ratings += 1
        self.average_rating = round(
            (self.average_rating * (self.count_of_ratings - 1) + rating)
            / self.count_of_ratings, 1
        )

    def serve_cars(self, cars: list) -> float:
        incomes = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                incomes += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(incomes, 1)

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
            average_rating: int,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center,
            1,
        )

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, car: list[Car]) -> float:
        income = 0
        for car_wash in car:
            if self.clean_power > car_wash.clean_mark:
                income += self.calculate_washing_price(car_wash)
                self.wash_single_car(car_wash)
        return round(income, 1)

    def rate_service(self, new_rate: float) -> None:
        self.average_rating = round(
            (
                self.average_rating
                * self.count_of_ratings
                + new_rate
            )
            / (self.count_of_ratings + 1),
            1,
        )
        self.count_of_ratings += 1

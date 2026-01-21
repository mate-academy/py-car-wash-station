class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        if not 1 <= comfort_class <= 7:
            raise ValueError
        if not 1 <= clean_mark <= 10:
            raise ValueError

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
        if not 1.0 <= distance_from_city_center <= 10.0:
            raise ValueError
        if not 1 <= clean_power <= 10:
            raise ValueError
        if not 1.0 <= average_rating <= 5.0:
            raise ValueError
        if count_of_ratings < 0:
            raise ValueError

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center,
            1
        )

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, upd_rating: int) -> None:
        if not 1 <= upd_rating <= 5:
            raise ValueError
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + upd_rating)
            / (self.count_of_ratings + 1),
            1
        )
        self.count_of_ratings += 1

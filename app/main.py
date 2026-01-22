class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str)\
            -> None:
        self.comfort_class, self.clean_mark, self.brand = (
            comfort_class,
            clean_mark,
            brand,
        )


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:

        (
            self.distance_from_city_center,
            self.clean_power,
            self.average_rating,
            self.count_of_ratings,
        ) = (
            distance_from_city_center,
            clean_power,
            average_rating,
            count_of_ratings
        )

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * (self.average_rating / self.distance_from_city_center),
            1,
        )

    def serve_cars(self, cars: list[Car]) -> float:
        amount = round(
            sum(
                self.calculate_washing_price(car)
                for car in cars
                if car.clean_mark < self.clean_power
            ),
            1,
        )

        for car in cars:
            self.wash_single_car(car)
        return amount

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float | int) -> None:
        self.average_rating = round(
            ((self.count_of_ratings * self.average_rating) + rate)
            / (self.count_of_ratings + 1),
            1,
        )
        self.count_of_ratings += 1

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
        count_of_ratings: int,
    ) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(
        self,
        car: Car,
    ) -> float:
        clean_rate = self.clean_power - car.clean_mark
        return round(
            (
                car.comfort_class
                * clean_rate
                * self.average_rating
                / self.distance_from_city_center
            ),
            1
        )

    def serve_cars(self, cars: list[Car]) -> float:
        income_cash = 0
        for car in cars:
            income_cash += self.wash_single_car(car)
        return round(income_cash, 1)

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            income_cash = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return income_cash
        return 0

    def rate_service(self, rate: float) -> None:
        self.count_of_ratings += 1
        self.average_rating = round(
            (self.average_rating * (self.count_of_ratings - 1) + rate)
            / self.count_of_ratings,
            1,
        )

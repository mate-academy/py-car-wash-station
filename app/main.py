class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        if not (1 <= comfort_class <= 7):
            raise ValueError("comfort_class must be from 1 to 7")
        if not (1 <= clean_mark <= 10):
            raise ValueError("clean_mark must be from 1 to 10")

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
        if not (1.0 <= distance_from_city_center <= 10.0):
            raise ValueError("distance_from_city_center must be from 1 to 10")
        if not (1 <= clean_power <= 10):
            raise ValueError("clean_power must be from 1 to 10")
        if not (1.0 <= average_rating <= 5.0):
            raise ValueError("average_rating must be from 1.0 to 5.0")

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            (
                car.comfort_class
                * (self.clean_power - car.clean_mark)
                * self.average_rating
            ) / self.distance_from_city_center,
            1
        ) if car.clean_mark < self.clean_power else 0

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        total_rates_before_rate = self.count_of_ratings * self.average_rating
        self.count_of_ratings += 1
        self.average_rating = round(
            ((total_rates_before_rate + rate) / self.count_of_ratings), 1
        )

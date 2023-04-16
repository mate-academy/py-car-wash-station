class Car:
    def __init__(
        self, comfort_class: int, clean_mark: int, brand: str
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

    def serve_cars(self, cars: list[Car]) -> float:
        money = 0
        income = (money + self.wash_single_car(car) for car in cars)
        return sum(income)

    def calculate_washing_price(self, auto: Car) -> float:
        return round(
            auto.comfort_class
            * (self.clean_power - auto.clean_mark)
            * self.average_rating
            / self.distance_from_city_center,
            1,
        )

    def wash_single_car(self, auto: Car) -> float:
        money = 0
        if auto.clean_mark < self.clean_power:
            money = self.calculate_washing_price(auto)
            auto.clean_mark = self.clean_power
        return money

    def rate_service(self, rate: float) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rate)
            / (self.count_of_ratings + 1),
            1,
        )
        self.count_of_ratings += 1

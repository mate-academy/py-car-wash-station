class Car:
    __slots__ = ("comfort_class", "clean_mark", "brand")

    def __init__(
            self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    __slots__ = (
        "distance_from_city_center",
        "clean_power",
        "average_rating",
        "count_of_ratings"
    )

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

    def serve_cars(self, cars: list[Car]) -> int:
        income = 0
        for car in cars:
            if self.wash_single_car(car.clean_mark):
                price = self.calculate_washing_price(car)
                income += price
                car.clean_mark = self.clean_power
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        return (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )

    def wash_single_car(self, clean_mark: int) -> bool:
        return clean_mark <= self.clean_power

    def rate_service(self, single_rate: int) -> None:
        amount_rate = self.average_rating * self.count_of_ratings + single_rate
        self.average_rating = round(
            amount_rate / (self.count_of_ratings + 1),
            1
        )
        self.count_of_ratings += 1

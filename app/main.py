class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: int | float,
        clean_power: int,
        average_rating: int | float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: object) -> float:
        difference = self.clean_power - car.clean_mark
        if difference <= 0:
            return 0.0
        return round(
            (
                car.comfort_class
                * difference
                * self.average_rating
                / self.distance_from_city_center
            ),
            1,
        )

    def wash_single_car(self, car: object) -> object:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                income += price
                self.wash_single_car(car)
        return round(income, 1)

    def rate_service(self, rate: int) -> None:
        numerator = self.average_rating * self.count_of_ratings + rate
        denominator = self.count_of_ratings + 1
        new_average_rating = numerator / denominator
        self.average_rating = round(new_average_rating, 1)
        self.count_of_ratings += 1

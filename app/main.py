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

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                washing_price = self.calculate_washing_price(car)
                income += washing_price
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, single_car: tuple) -> float:
        if self.clean_power > single_car.clean_mark:
            single_car_cost = (
                single_car.comfort_class
                * (self.clean_power - single_car.clean_mark)
                * self.average_rating
                / self.distance_from_city_center
            )
            return round(single_car_cost, 1)
        return 0.0

    def wash_single_car(self, car: tuple) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> float:
        self.average_rating = (round(
            (self.count_of_ratings * self.average_rating + rating)
            / (self.count_of_ratings + 1), 1)
        )
        self.count_of_ratings += 1
        return self.average_rating

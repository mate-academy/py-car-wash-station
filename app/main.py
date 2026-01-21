class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: int,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += round(
                    CarWashStation.calculate_washing_price(self, car), 1
                )
                CarWashStation.wash_single_car(self, car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        clean_difference = self.clean_power - car.clean_mark
        washing_price = (
            car.comfort_class
            * clean_difference
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(washing_price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        initial_count_of_rating = self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round(
            (self.average_rating
             * initial_count_of_rating
             + rate)
            / self.count_of_ratings, 1)

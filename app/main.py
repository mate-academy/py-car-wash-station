class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

    def __repr__(self) -> str:
        return f"Car(" \
               f"comfort_class = {self.comfort_class}, " \
               f"clean_mark = {self.clean_mark}, " \
               f"brand = {self.brand}"


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def __repr__(self) -> str:
        return f"CarWashStation(" \
               f"distance = {self.distance_from_city_center}, " \
               f"clean_power = {self.clean_power}, " \
               f"average_rating = {self.average_rating}, " \
               f"count_of_ratings = {self.count_of_ratings}"

    def serve_cars(self, cars: list) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class
                     * (abs(self.clean_power - car.clean_mark))
                     * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, mark: float) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + mark)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

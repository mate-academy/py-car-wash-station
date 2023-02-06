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
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars_list: list) -> float:
        income = 0
        for car in cars_list:
            if self.car_is_allowed_to_wash(car):
                income += round(self.calculate_washing_price(car), 1)
                self.wash_single_car(car)

        return income

    def calculate_washing_price(self, car: Car) -> float:

        washing_price = ((car.comfort_class
                          * (self.clean_power - car.clean_mark))
                         * (self.average_rating
                            / self.distance_from_city_center))

        return round(washing_price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.car_is_allowed_to_wash(car):
            car.clean_mark = self.clean_power

    def car_is_allowed_to_wash(self, car: Car) -> bool:
        return self.clean_power > car.clean_mark

    def rate_service(self, rate: float) -> None:
        overall_rate = ((self.count_of_ratings * self.average_rating + rate)
                        / (self.count_of_ratings + 1))

        self.count_of_ratings += 1
        self.average_rating = round(overall_rate, 1)

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

    def serve_cars(self, cars_list: list[Car]) -> float:
        income = 0
        for car in cars_list:
            if self.car_is_allowed_to_wash(car):
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return income

    def calculate_washing_price(self, car: Car) -> float:
        comfort_and_clean_factor = (car.comfort_class
                                    * (self.clean_power - car.clean_mark))

        rating_distance_factor = (self.average_rating
                                  / self.distance_from_city_center)

        washing_price = comfort_and_clean_factor * rating_distance_factor

        return round(washing_price, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def car_is_allowed_to_wash(self, car: Car) -> bool:
        return self.clean_power > car.clean_mark

    def rate_service(self, rate: float) -> None:
        sum_of_rates = (self.count_of_ratings * self.average_rating + rate)
        self.count_of_ratings += 1
        overall_rate = (sum_of_rates / self.count_of_ratings)
        self.average_rating = round(overall_rate, 1)

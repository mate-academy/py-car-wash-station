from typing import List


class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str,
    ) -> None:
        if 1 <= comfort_class <= 7:
            self.comfort_class = comfort_class
        else:
            self.comfort_class = 1

        if 1 <= clean_mark <= 10:
            self.clean_mark = clean_mark
        else:
            self.clean_mark = 1

        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: int,
            count_of_ratings: int
    ) -> None:
        if 1.0 <= distance_from_city_center <= 10.0:
            self.distance_from_city_center = distance_from_city_center
        else:
            self.distance_from_city_center = 1.0

        self.clean_power = clean_power

        if 1.0 <= average_rating <= 5.0:
            self.average_rating = average_rating
        else:
            self.average_rating = 1.0

        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        income_counter = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income_counter += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income_counter, 1)

    def calculate_washing_price(self, cars: Car) -> float:
        return round((
            cars.comfort_class
            * (self.clean_power - cars.clean_mark)
            * self.average_rating)
            / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        self.average_rating = round(((
                                    self.average_rating
                                    * self.count_of_ratings) + rate)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

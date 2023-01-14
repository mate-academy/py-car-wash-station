from typing import List


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
        distance_from_city_center: int,
        clean_power: int,
        average_rating: int,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings
        # car = Car

    def serve_cars(self, cars: List[Car]) -> float:
        price = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(price, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, one_car: Car) -> None:
        if one_car.clean_mark < self.clean_power:
            one_car.clean_mark = self.clean_power

    def rate_service(self, mark: float) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + mark)
            / (self.count_of_ratings + 1), 1,
        )
        self.count_of_ratings += 1

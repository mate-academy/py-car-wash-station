from typing import Union


class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self, distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            wash = self.wash_single_car(car)
            if wash:
                price, difference = self.calculate_washing_price(car)
                income += price
                car.clean_mark += difference
        return income

    def calculate_washing_price(self, car: Car) -> tuple[float, int]:
        difference = self.clean_power - car.clean_mark
        price = round(((car.comfort_class
                        * difference * self.average_rating)
                       / self.distance_from_city_center), 1)
        return price, difference

    def wash_single_car(self, car: Car) -> bool:
        if car.clean_mark <= self.clean_power:
            return True

    def rate_service(self, rate: Union[int, float]) -> None:
        self.count_of_ratings += 1
        self.average_rating = round((self.average_rating
                                     * (self.count_of_ratings - 1) + rate)
                                    / self.count_of_ratings, 1)

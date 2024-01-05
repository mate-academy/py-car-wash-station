from typing import Callable


class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: Callable) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Callable) -> float:
        print(car.clean_mark, self.clean_power)
        if car.clean_mark < self.clean_power:
            washing_price = (car.comfort_class
                             * (self.clean_power - car.clean_mark)
                             * self.average_rating / self.distance_from_city)
        else:
            washing_price = 0
        return round(washing_price, 1)

    def serve_cars(self, cars_list: list) -> float:
        income_price_list = []
        for car in cars_list:
            price_one_car = self.calculate_washing_price(car)
            income_price_list.append(price_one_car)
            self.wash_single_car(car)
        return sum(income_price_list)

    def rate_service(self, rate: float) -> None:
        new_rate = ((self.average_rating * self.count_of_ratings + rate)
                    / (self.count_of_ratings + 1))
        self.average_rating = round(new_rate, 1)
        self.count_of_ratings += 1

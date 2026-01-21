from typing import List


class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    __ROUNDING_PRECISION = 1

    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        income = 0

        for car in cars:
            if self.__is_car_valid(car):
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(income, CarWashStation.__ROUNDING_PRECISION)

    def rate_service(self, single_rate: int) -> None:
        total_rate = self.average_rating * self.count_of_ratings
        total_rate += single_rate
        self.count_of_ratings += 1
        self.average_rating = round(
            total_rate / self.count_of_ratings,
            CarWashStation.__ROUNDING_PRECISION)

    def wash_single_car(self, car: Car) -> None:
        if self.__is_car_valid(car):
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            (car.comfort_class * (self.clean_power - car.clean_mark)
             * self.average_rating / self.distance_from_city_center),
            CarWashStation.__ROUNDING_PRECISION)

    def __is_car_valid(self, car: Car) -> bool:
        return car.clean_mark < self.clean_power

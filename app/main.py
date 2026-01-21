from typing import Any


class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

    @classmethod
    def __check_class(cls, comfort_class: int) -> bool:
        return comfort_class in range(1, 8)

    @classmethod
    def __check_mark(cls, clean_mark: int) -> bool:
        return clean_mark in range(1, 11)

    @property
    def comfort_class(self) -> Any:
        return self._comfort_class

    @property
    def clean_mark(self) -> Any:
        return self._clean_mark

    @comfort_class.setter
    def comfort_class(self, comfort_class: int) -> None:
        if not self.__check_class(comfort_class):
            raise ValueError("Error: comfort class should be in range 1 - 7")
        else:
            self._comfort_class = comfort_class

    @clean_mark.setter
    def clean_mark(self, clean_mark: int) -> None:
        if not self.__check_mark(clean_mark):
            raise ValueError("Error: clean mark should be in range 1 - 10")
        else:
            self._clean_mark = clean_mark

    def car_washed(self, station_power: int) -> None:
        self.clean_mark = station_power


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

    @classmethod
    def __check_distance(cls, distance_from_city_center: float) -> bool:
        return 1.0 <= distance_from_city_center <= 10.0

    @classmethod
    def __check_station_rating(cls, average_rating: float) -> bool:
        return 1.0 <= average_rating <= 5.0

    @property
    def average_rating(self) -> Any:
        return self._average_rating

    @property
    def distance_from_city_center(self) -> Any:
        return self._distance_from_city_center

    @average_rating.setter
    def average_rating(self, value: float) -> None:
        if not self.__check_station_rating(value):
            raise ValueError("Average station rating should be "
                             "in range: 1.0 - 5.0")
        else:
            self._average_rating = value

    @distance_from_city_center.setter
    def distance_from_city_center(self, value: float) -> None:
        if not self.__check_distance(value):
            raise ValueError("distance to city should be "
                             "in range: 1.0 - 10.0 km.")
        else:
            self._distance_from_city_center = value

    def serve_cars(self, cars_ls: list[Car]) -> float:
        income = 0

        for car in cars_ls:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = round(car.comfort_class
                      * (self.clean_power - car.clean_mark)
                      * self.average_rating
                      / self.distance_from_city_center, 1)

        return price

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.car_washed(self.clean_power)

    def rate_service(self, value: float) -> None:
        if 0.0 <= value <= 5.0:
            raiting_sum = (self.average_rating * self.count_of_ratings) + value
            self.count_of_ratings += 1
            self.average_rating = round(raiting_sum / self.count_of_ratings, 1)
        else:
            raise ValueError("Value of raining should be in range: 0 - 5")

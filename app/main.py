from typing import Callable


class Car:
    def __init__(
        self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:  # noqa: E501
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

    @property
    def comfort_class(self) -> int:
        return self._comfort_class

    @comfort_class.setter
    def comfort_class(self, value: int) -> None:
        if value < 1:
            self._comfort_class = 1
        elif value > 7:
            self._comfort_class = 7
        else:
            self._comfort_class = value

    @property
    def clean_mark(self) -> int:
        return self._clean_mark

    @clean_mark.setter
    def clean_mark(self, value: int) -> None:
        if value < 1:
            self._clean_mark = 1
        elif value > 10:
            self._clean_mark = 10
        else:
            self._clean_mark = value


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: int,
        clean_power: int,
        average_rating: int,
        count_of_ratings: int,  # noqa: E501
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
        self.calculate_price_muliplayer()

    @property
    def distance_from_city_center(self) -> float:
        return self._distance_from_city_center

    @distance_from_city_center.setter
    def distance_from_city_center(self, value: int) -> None:
        if value < 1:
            self._distance_from_city_center = 1
        elif value > 10:
            self._distance_from_city_center = 10
        else:
            self._distance_from_city_center = value

    @property
    def average_rating(self) -> float:
        return self._average_rating

    @average_rating.setter
    def average_rating(self, value: int) -> None:
        if value < 1:
            self._average_rating = 1
        elif value > 5:
            self._average_rating = 5
        else:
            self._average_rating = round(value, 1)

    def serve_cars(self, cars: list[Car]) -> float:
        cars = self.filter_cars(cars, self.validate_car)

        income = 0

        for car in cars:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)

        return round(income, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rate)
            / (self.count_of_ratings + 1),
            1,
        )
        self.count_of_ratings += 1

        self.calculate_price_muliplayer()

    def validate_car(self, car: Car) -> bool:
        return car.clean_mark < self.clean_power

    def filter_cars(self, cars: list[Car], filter_fun: Callable) -> list[Car]:
        return [car for car in cars if filter_fun(car)]

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class
            * self.calculate_car_multiplayer(car)
            * self.price_multiplayer,
            1,
        )

    def calculate_price_muliplayer(self) -> None:
        self.price_multiplayer = (
            self.average_rating / self.distance_from_city_center
        )  # noqa: E501

    def calculate_car_multiplayer(self, car: Car) -> int:
        return self.clean_power - car.clean_mark

from typing import Union


class Car:
    def __init__(self,
                 comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: Union[float, int],
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def can_we_wash_car(self, car: Car) -> bool:
        """
        returns True if station.clean_power > car.clean mark else False
        """
        return self.clean_power > car.clean_mark

    def serve_cars(self, cars: list) -> float:
        total_income = 0
        for car in cars:
            if self.can_we_wash_car(car):
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return total_income

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            (self.clean_power - car.clean_mark)
            * car.comfort_class
            * self.average_rating
            / self.distance_from_city_center,
            1,
        )

    def wash_single_car(self, car: Car) -> None:
        if self.can_we_wash_car(car):
            car.clean_mark = self.clean_power

    def rate_service(self, mark: Union[float, int]) -> float:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + mark)
            / (self.count_of_ratings + 1),
            1,
        )
        self.count_of_ratings += 1
        return self.average_rating

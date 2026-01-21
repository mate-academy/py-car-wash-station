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
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> int | float:
        total_income = 0
        for car in cars:
            income = self.calculate_washing_price(car)
            total_income += income
            self.wash_single_car(car)
        return total_income

    def wash_single_car(self, car: Car) -> int:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
            return car.clean_mark

    def calculate_washing_price(self, car: Car) -> int | float:
        if car.clean_mark >= self.clean_power:
            return 0
        price_wash_ = (car.comfort_class
                       * (self.clean_power - car.clean_mark)
                       * self.average_rating
                       / self.distance_from_city_center)
        price_wash = round(price_wash_, 1)
        return price_wash

    def rate_service(self, rate: int) -> int | float:
        self.average_rating = round((self.average_rating
                                     * self.count_of_ratings + rate)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings = self.count_of_ratings + 1
        return self.average_rating, self.count_of_ratings

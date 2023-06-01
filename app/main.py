from typing import List


class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: float, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: float,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        amount = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                amount += (car.comfort_class
                           * (self.clean_power - car.clean_mark)
                           * (self.average_rating
                              / self.distance_from_city_center))
                car.clean_mark = self.clean_power
        return round(amount, 1)

    def calculate_washing_price(self, cars: List[Car]) -> float:
        for car in cars:
            w_price = (car.comfort_class
                       * (self.clean_power - car.clean_mark)
                       * (self.average_rating
                          / self.distance_from_city_center))
            return round(w_price, 1)

    def wash_single_car(self, cars: List[Car]) -> float:
        for car in cars:
            if car.clean_mark < self.clean_power:
                car.clean_mark = self.clean_power
                return car.clean_mark
            else:
                return car.clean_mark

    def rate_service(self, single_rate: float) -> float:
        rating = ((self.average_rating
                   * self.count_of_ratings + single_rate)
                  / (self.count_of_ratings + 1))
        return round(rating, 1)

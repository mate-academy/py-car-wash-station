from typing import Union


class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_income(self, car: Car) -> Union[float, int]:
        price = (round((car.comfort_class
                        * (self.clean_power - car.clean_mark)
                        * self.average_rating
                        / self.distance_from_city_center), 1))
        return price

    def calculate_washing_price(self, car: Car) -> Union[float, int]:
        return self.calculate_income(car)

    def wash_single_car(self, car: Car) -> Union[float, int]:
        price = 0
        if car.clean_mark <= self.clean_power:
            price += self.calculate_income(car)
            car.clean_mark = self.clean_power
            return price
        else:
            return 0

    def serve_cars(self, cars: list[Car]) -> Union[float, int]:
        total_price = 0
        for car in cars:
            total_price += self.wash_single_car(car)
        return total_price

    def rate_service(self, rate: int) -> None:
        self.count_of_ratings += 1
        self.average_rating = round((self.average_rating
                                     * (self.count_of_ratings - 1)
                                     + rate) / self.count_of_ratings, 1)

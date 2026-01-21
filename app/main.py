from typing import Any


class Car:
    def __init__(self, comfort_class: int | float,
                 clean_mark: int | float,
                 brand: int | float) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


car = Car(comfort_class=0, clean_mark=0, brand=0)


class CarWashStation:
    def __init__(self, distance_from_city_center: int | float,
                 clean_power: int | float,
                 average_rating: int | float,
                 count_of_ratings: int | float) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, class_car_instance: Car) -> Any:
        return (round(class_car_instance.comfort_class
                * (self.clean_power - class_car_instance.clean_mark)
                * self.average_rating / self.distance_from_city_center, 1))

    def wash_single_car(self, class_car_instance: Car) -> Any:
        if class_car_instance.clean_mark <= self.clean_power:
            single_car_price = self.calculate_washing_price(class_car_instance)
            class_car_instance.clean_mark = self.clean_power
            return single_car_price

    def serve_cars(self, cars_list: list) -> Any:
        income = 0
        for unit in cars_list:
            if unit.clean_mark < self.clean_power:
                income += self.wash_single_car(unit)
                unit.clean_mark = self.clean_power
        return income

    def rate_service(self, single_rate: int | float) -> Any:
        total = round(self.average_rating * self.count_of_ratings, 1)
        self.count_of_ratings += 1
        self.average_rating = (round((total + single_rate)
                                     / self.count_of_ratings, 1))
        return self.average_rating

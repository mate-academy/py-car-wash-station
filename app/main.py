from __future__ import annotations


class Car:

    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += round(self.calculate_washing_price(car), 1)
                self.wash_single_car(car)
        print(income)
        return income

    def calculate_washing_price(self, car: Car):
        price = car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center
        return price

    def wash_single_car(self, car: Car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rate: int):
        self.count_of_ratings += 1
        self.average_rating = round((self.average_rating * (self.count_of_ratings - 1) + new_rate) / self.count_of_ratings, 1)


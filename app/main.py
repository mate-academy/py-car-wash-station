from typing import List


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

    def serve_cars(self, cars: List[Car]):
        amount = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                amount += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return amount

    def calculate_washing_price(self, car: Car):
        profit_for_one_car = (car.comfort_class * (self.clean_power - car.clean_mark) * (
                    self.average_rating / self.distance_from_city_center))
        return round(profit_for_one_car, 1)
# 3

    def wash_single_car(self, car):
        if self.clean_power >= car.clean_mark:
            car.clean_mark = self.clean_power
            return car.clean_mark

    def rate_service(self, mark):
        self.average_rating = round((self.average_rating * self.count_of_ratings + mark) / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
        return self.average_rating

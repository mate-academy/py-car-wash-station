class Car:

    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(
            self,
            distance_from_city_center,
            clean_power,
            average_rating,
            count_of_ratings
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, Car):
        incom = 0
        for car in Car:
            if self.clean_power > car.clean_mark:
                incom += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
        return incom

    def calculate_washing_price(self, cars):
        return round(
            cars.comfort_class * (
                self.clean_power - cars.clean_mark) * (
                self.average_rating / self.distance_from_city_center),
            1)

    def wash_single_car(self, auto):
        if auto.clean_mark < self.clean_power:
            auto.clean_mark = self.clean_power
        return auto.clean_mark

    def rate_service(self, number):
        sum_of_all_grades = self.average_rating * self.count_of_ratings
        sum_of_all_grades += number
        self.count_of_ratings += 1
        self.average_rating = round(
            (sum_of_all_grades / self.count_of_ratings),
            1)
        return self.average_rating

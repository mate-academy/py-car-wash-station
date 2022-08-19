class Car:
    def __init__(self, comfort_class: float, clean_mark: float, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: float,
                 average_rating: float, count_of_ratings: float):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car):
        if self.clean_power >= car.clean_mark:
            amount = round(car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating /
                           self.distance_from_city_center, 1)
            return amount

    def serve_cars(self, cars: list):
        amount = 0
        for i in cars:
            if self.clean_power >= i.clean_mark:
                amount += round(i.comfort_class * (self.clean_power - i.clean_mark) * self.average_rating /
                                self.distance_from_city_center, 1)
                i.clean_mark = self.clean_power
        return amount

    def wash_single_car(self, car: Car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int):
        self.average_rating = round((self.average_rating * self.count_of_ratings + rate) /
                                    (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

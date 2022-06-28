class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        income = 0
        for car in cars:
            income += self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car):
        car_class = car.comfort_class
        diff = self.clean_power - car.clean_mark
        av_rate = self.average_rating
        dist = self.distance_from_city_center
        if diff > 0:
            wash_price = round(car_class * diff * av_rate / dist, 1)
        else:
            wash_price = 0
        return wash_price

    def wash_single_car(self, car):
        wash_cost = self.calculate_washing_price(car)
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        return wash_cost

    def rate_service(self, rate: int):
        self.count_of_ratings += 1
        av_rate = self.average_rating
        count = self.count_of_ratings
        self.average_rating = round(av_rate + (rate - av_rate) / count, 1)

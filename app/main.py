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

    def car_for_wash(self, cars: list) -> list:
        return [car for car in cars if car.clean_mark < self.clean_power]

    def serve_cars(self, cars: list):
        cars_for_wash = self.car_for_wash(cars)
        income = 0
        for car in cars_for_wash:
            income += self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
        return income

    def calculate_washing_price(self, car: Car):
        wash_cost = car.comfort_class * (self.clean_power - car.clean_mark) \
                    * self.average_rating / self.distance_from_city_center
        return round(wash_cost, 1)

    def wash_single_car(self, car: Car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
        return self.clean_power

    def rate_service(self, rate):
        av_rating = (self.count_of_ratings * self.average_rating + rate) / (self.count_of_ratings + 1)
        self.average_rating = round(av_rating, 1)
        self.count_of_ratings += 1

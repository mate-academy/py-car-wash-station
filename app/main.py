class Car:

    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self, distance_from_city_center: float,
                 clean_power: float,
                 average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        profit = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                profit += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
        return round(profit, 1)

    def calculate_washing_price(self, car: Car):
        comfort_diff = car.comfort_class * (self.clean_power - car.clean_mark)
        rating_dist = (self.average_rating / self.distance_from_city_center)
        return round(comfort_diff * rating_dist, 1)

    def wash_single_car(self, car: Car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate):
        average_rate = self.count_of_ratings * self.average_rating
        number_of_points = average_rate + rate
        self.count_of_ratings += 1
        rating = round(number_of_points / self.count_of_ratings, 1)
        self.average_rating = rating

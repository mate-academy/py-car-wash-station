class Car:
    def __init__(
            self,
            comfort_class,
            clean_mark,
            brand):
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

    def serve_cars(self, cars):
        profit = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                profit += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return profit

    def calculate_washing_price(self, car: Car):
        result = car.comfort_class * (self.clean_power - car.clean_mark)
        return round(
            (result * self.average_rating / self.distance_from_city_center),
            1)

    def wash_single_car(self, cars):
        if self.clean_power >= cars.clean_mark:
            cars.clean_mark = self.clean_power
            
    def rate_service(self, rate):
        res = self.count_of_ratings * self.average_rating + rate
        self.count_of_ratings = self.count_of_ratings + 1
        self.average_rating = round(res / (self.count_of_ratings), 1)

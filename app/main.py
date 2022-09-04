class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            dist_from_city_center,
            clean_power,
            average_rating,
            count_of_ratings
    ):
        self.distance_from_city_center = dist_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        price = car.comfort_class * (self.clean_power - car.clean_mark)\
            * self.average_rating / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, auto):
        if auto.clean_mark < self.clean_power:
            auto.clean_mark = self.clean_power

    def serve_cars(self, cars):
        res = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                res += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
        return res

    def rate_service(self, rate):
        sum_of_first_rates = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        res = (sum_of_first_rates / self.count_of_ratings)
        self.average_rating = round(res, 1)

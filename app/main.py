class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        if 1 <= comfort_class <= 7:
            self.comfort_class = comfort_class
        if 1 <= clean_mark <= 10:
            self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power,
                 average_rating, count_of_ratings):
        if 1.0 <= distance_from_city_center <= 10.0:
            self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        if 1.0 <= average_rating <= 5.0:
            self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        sum_price = 0
        for car in cars:
            if car.clean_mark <= self.clean_power:
                sum_price += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return sum_price

    def calculate_washing_price(self, car: Car):
        return round(car.comfort_class * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car):
        if car.clean_mark <= self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int):
        self.average_rating = \
            round((self.average_rating * self.count_of_ratings + rate)
                  / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

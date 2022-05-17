class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power,
                 average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        price = car.comfort_class * (self.clean_power - car.clean_mark)\
            * self.average_rating / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate):
        new_avg_rating = (self.count_of_ratings * self.average_rating + rate)\
            / (self.count_of_ratings + 1)
        self.average_rating = round(new_avg_rating, 1)
        self.count_of_ratings += 1

    def serve_cars(self, cars_list):
        value = 0
        for car in cars_list:
            if car.clean_mark < self.clean_power:
                value += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
        return value

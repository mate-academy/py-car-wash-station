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

    def rate_service(self, rate):
        self.average_rating = ((self.count_of_ratings * self.average_rating + rate)
                               / (self.count_of_ratings + 1))
        self.count_of_ratings += 1

    def wash_single_car(self, car: Car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car):
        return round((car.comfort_class * (self.clean_power - car.clean_mark) *
                     self.average_rating) / self.distance_from_city_center, 1)

    def serve_cars(self, car_list):
        total_income = 0
        for car in car_list:
            if car.clean_mark < self.clean_power:
                self.wash_single_car(car)
                washing_price = self.calculate_washing_price(car)
                total_income += washing_price
        return round(total_income, 1)

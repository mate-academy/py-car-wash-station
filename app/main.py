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
    def calculate_washing_price(self, car):
        difference = self.clean_power - car.clean_mark
        if difference <= 0:
            return 0.0
        price = car.comfort_class * difference * self.average_rating / self.distance_from_city_center
        return round(price, 1)
    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
    def serve_cars(self, cars_list):
        income = 0.0
        for car in cars_list:
            price = self.calculate_washing_price(car)
            if price > 0:
                self.wash_single_car(car)
                income += price
        return  round(income, 1)
    def rate_service(self, rate):
        total_score = self.average_rating * self.count_of_ratings
        total_score += rate
        self.count_of_ratings += 1
        self.average_rating = round(total_score / self.count_of_ratings, 1)


class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self. clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        amount = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                amount += car.comfort_class * (self.clean_power - car.clean_mark) * \
                          (self.average_rating/self.distance_from_city_center)
                car.clean_mark = self.clean_power
        return round(amount, 1)

    def calculate_washing_price(self, cars):
        for car in cars:
            w_price = car.comfort_class * (self.clean_power - car.clean_mark) * \
                      (self.average_rating/self.distance_from_city_center)
            return round(w_price, 1)

    def wash_single_car(self, cars):
        for car in cars:
            if car.clean_mark < self.clean_power:
                car.clean_mark = self.clean_power
                return car.clean_mark
            else:
                return car.clean_mark

    def rate_service(self, single_rate):
        rating = (self.average_rating * self.count_of_ratings + single_rate) / (self.count_of_ratings + 1)
        return round(rating, 1)









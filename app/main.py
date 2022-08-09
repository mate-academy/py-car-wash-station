class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power_clean_mark,
                 average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power_clean_mark = clean_power_clean_mark
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power_clean_mark:
                income += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power_clean_mark
        return income

    def calculate_washing_price(self, car):
        price = round(((car.comfort_class * (self.clean_power_clean_mark - car.
                                             clean_mark) * self.
                        average_rating) / self.
                       distance_from_city_center), 1)
        return price

    def wash_single_car(self, cars):
        for car in cars:
            if car.clean_mark < self.clean_power_clean_mark:
                clean_mark = self.clean_power_clean_mark
        return clean_mark

    def rate_service(self, number):
        self.average_rating = \
            round(((self.average_rating * self.
                    count_of_ratings) + number) / (self.
                                                   count_of_ratings + 1), 1)
        self.count_of_ratings = self.count_of_ratings + 1
        return self.average_rating

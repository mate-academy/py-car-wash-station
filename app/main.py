class Car:

    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self,
                 distance_from_city_center,
                 clean_power, average_rating,
                 count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
        self.income = 0

    def serve_cars(self, cars: list):
        for car in cars:
            if car.clean_mark < self.clean_power:
                self.wash_single_car(car)
        return self.income

    def calculate_washing_price(self, car):
        price = car.comfort_class * \
            (self.clean_power - car.clean_mark) * \
            (self.average_rating / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car):
        self.income += self.calculate_washing_price(car)
        car.clean_mark = self.clean_power

    def rate_service(self, mark):
        new_sum_of_rating = \
            self.average_rating * self.count_of_ratings + mark
        self.average_rating = \
            round(
                new_sum_of_rating / (self.count_of_ratings + 1),
                1)
        self.count_of_ratings += 1
        return self.average_rating

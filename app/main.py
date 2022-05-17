class Car:
    def __init__(self, comfort_class, clean_mark, brand):
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

    def serve_cars(self, list_cars):
        income = 0
        for car in list_cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, single_car):
        price = single_car.comfort_class * \
            (self.clean_power - single_car.clean_mark) \
            * self.average_rating / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, single_car):
        if single_car.clean_mark < self.clean_power:
            single_car.clean_mark = self.clean_power

    def rate_service(self, rate):
        self.count_of_ratings += 1
        n_rate = ((self.average_rating * (self.count_of_ratings - 1)) + rate) \
            / self.count_of_ratings
        self.average_rating = round(n_rate, 1)

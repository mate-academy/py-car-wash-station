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

    def rate_service(self, rate):
        rates = self.average_rating * self.count_of_ratings
        rates += rate
        self.count_of_ratings += 1
        self.average_rating = round(rates / self.count_of_ratings, 1)

    def wash_single_car(self, auto):
        if auto.clean_mark < self.clean_power:
            auto.clean_mark = self.clean_power

    def calculate_washing_price(self, auto):
        price = auto.comfort_class
        price *= self.clean_power - auto.clean_mark
        price *= self.average_rating
        price /= self.distance_from_city_center
        return round(price, 1)

    def serve_cars(self, cars):
        count = 0
        for auto in cars:
            if auto.clean_mark < self.clean_power:
                count += self.calculate_washing_price(auto)
                self.wash_single_car(auto)
        return round(count, 1)

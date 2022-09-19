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

    def serve_cars(self, cars):
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car):
        distance = self.distance_from_city_center
        if car.clean_mark < self.clean_power:
            price_clean = self.clean_power - car.clean_mark
            price_comfort_and_clean = car.comfort_class * price_clean
            price_distance_and_rating = self.average_rating / distance
            income1 = price_comfort_and_clean * price_distance_and_rating
            return round(income1, 1)
        return 0

    def rate_service(self, rate):
        total_rate = self.count_of_ratings / (self.count_of_ratings + 1
                                              ) * self.average_rating
        how_many_gives_one_rate = 1 / (self.count_of_ratings + 1) * rate
        self.average_rating = round((total_rate + how_many_gives_one_rate), 1)
        self.count_of_ratings += 1

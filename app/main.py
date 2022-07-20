class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: float,
                 average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
        return round(income, 1)

    def calculate_washing_price(self, car):
        dif_clean = self.clean_power - car.clean_mark
        comfort_clean = car.comfort_class * dif_clean
        av_rating_clean = comfort_clean * self.average_rating
        wash_cost = round(av_rating_clean / self.distance_from_city_center, 1)
        return wash_cost

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate):
        gen_rate_count = self.average_rating * self.count_of_ratings
        curr_rate_count = gen_rate_count + rate
        self.average_rating = \
            round(curr_rate_count / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

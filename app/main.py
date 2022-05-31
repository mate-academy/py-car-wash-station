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

    def serve_cars(self, ls: list):
        inc = 0
        for i in ls:
            if i.clean_mark < self.clean_power:
                inc += self.calculate_washing_price(i)
                self.wash_single_car(i)
        return inc

    def calculate_washing_price(self, car):
        dict_rat_coef = self.average_rating / self.distance_from_city_center
        clean_coef = self.clean_power - car.clean_mark
        return round(car.comfort_class * clean_coef * dict_rat_coef, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark: int):
        av_sum = self.count_of_ratings * self.average_rating
        self.count_of_ratings += 1
        self.average_rating = round((av_sum + mark) / self.count_of_ratings, 1)

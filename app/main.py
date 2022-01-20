class Car:

    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power,
                 average_rating, count_of_rating):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_rating

    def serve_cars(self, cars_list: list):
        income = sum([self.calculate_washing_price(car) for car in cars_list
                      if car.clean_mark < self.clean_power])
        for car in cars_list:
            self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car):
        clean_dif = self.clean_power - car.clean_mark
        clean_ratio = self.average_rating / self.distance_from_city_center
        return round((car.comfort_class * clean_dif * clean_ratio), 1)

    def wash_single_car(self, car: Car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark: float):
        updated_rating = (self.average_rating * self.count_of_ratings + mark)
        self.count_of_ratings += 1
        self.average_rating = round(updated_rating / self.count_of_ratings, 1)

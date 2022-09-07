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

    def serve_cars(self, cars_list):
        result = 0
        for car in cars_list:
            if self.calculate_washing_price(car) is not None:
                result += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(result, 1)

    def calculate_washing_price(self, car):
        if car.clean_mark < self.clean_power:
            difference = self.clean_power - car.clean_mark
            income = \
                car.comfort_class * difference * self.average_rating / \
                self.distance_from_city_center
            return round(income, 1)

    def rate_service(self, mark):
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + mark) / (
                self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
        return self.average_rating

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
            return car.clean_mark

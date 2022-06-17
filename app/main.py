class Car:

    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation(Car):

    def __init__(self, distance_from_city_center, clean_power,
                 average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, other):
        if self.clean_power < other.clean_mark:
            return 0
        result = other.comfort_class * (self.clean_power - other.clean_mark)\
            * self.average_rating / self.distance_from_city_center
        return round(result, 1)

    def wash_single_car(self, other):
        if self.clean_power > other.clean_mark:
            other.clean_mark = self.clean_power
            return True

    def rate_service(self, mark):
        x = (self.average_rating * self.count_of_ratings + mark) /\
            (self.count_of_ratings + 1)
        x = round(x, 1)
        self.count_of_ratings += 1
        self.average_rating = x
        return x

    def serve_cars(self, income):
        serve_c = []
        for i in income:
            x = CarWashStation.calculate_washing_price(self, i)
            CarWashStation.wash_single_car(self, i)
            if x >= 0:
                serve_c.append(x)
        return sum(serve_c)

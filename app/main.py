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

    def rate_service(self, mark):
        calc_mark = (self.average_rating * self.count_of_ratings + mark) /\
                    (self.count_of_ratings + 1)
        calc_mark = round(calc_mark, 1)
        self.count_of_ratings += 1
        self.average_rating = calc_mark
        return calc_mark

    def serve_cars(self, ls_of_cars):
        serve_cost = []
        for car in ls_of_cars:
            calc = self.calculate_washing_price(car)
            self.wash_single_car(car)
            if calc >= 0:
                serve_cost.append(calc)
        return sum(serve_cost)

class Car:
    def __init__(self, c_c: int, c_m: int, brand: str):
        self.comfort_class = c_c
        self.clean_mark = c_m
        self.brand = brand


class CarWashStation:
    def __init__(self, d_f_c_c: float,
                 cl_p: int, av_rat: float,
                 c_of_rat: int):
        self.distance_from_city_center = d_f_c_c
        self.clean_power = cl_p
        self.average_rating = av_rat
        self.count_of_ratings = c_of_rat

    def serve_cars(self, cars: list):
        cost = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                cost += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(cost, 1)

    def calculate_washing_price(self, car):
        cost = car.comfort_class * (self.clean_power - car.clean_mark)
        cost *= self.average_rating / self.distance_from_city_center     # calculate cost of washing in 2 steps
        return round(cost, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate):
        self.average_rating =\
            round((rate + self.average_rating * self.count_of_ratings)
                  / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

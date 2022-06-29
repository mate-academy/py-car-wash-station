class Car:
    def __init__(self, comfort_class: int , clean_mark : int , brand : str):
        if 8 < self.comfort_class < 0:
            self.comfort_class = comfort_class

        if 10 < self.clean_mark < 1:
            self.clean_mark = clean_mark

        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power : int,
        average_rating: float,
        count_of_ratings: int
    ):
        if 10.0 < self.distance_from_city_center < 1.0:
            self.distance_from_city_center = distance_from_city_center

        if 5.0 < self.average_rating < 1.0:
            self.average_rating = average_rating

        self.count_of_ratings = count_of_ratings
        self.clean_power = Car.clean_mark

    def serve_cars(self, Car_list : list):
        return[car1 for car1 in Car_list if self.clean_power > car1.clean_mark]

    def calculate_washing_price(self , car1 : Car):
        clean_cars = car1.comfort_class * self.clean_power - car1.clean_mark
        a_div_dist = self.average_rating / self.distance_from_city_center
        return round(clean_cars * a_div_dist, 1)

    def wash_single_car(self, car1 : Car):
        if self.clean_power > car1.clean_mark:
            car1.clean_mark = self.clean_power

    def rate_service(self, car1: Car):
        self.mark = self.average_rating / self.count_of_ratings

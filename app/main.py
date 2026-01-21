class Car:
    def __init__(self, comfort_class: int , clean_mark : int , brand : str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power : int,
        average_rating: float,
        count_of_ratings: int,
    ):
        self.distance_from_city_center = distance_from_city_center
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
        self.clean_power = clean_power

    def serve_cars(self, car_list : list):
        amount = 0
        for car in car_list:
            if self.clean_power > car.clean_mark:
                amount += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(amount , 1)

    def calculate_washing_price(self , car : Car):
        clean_cars = car.comfort_class * (self.clean_power - car.clean_mark)
        a_div_dist = self.average_rating / self.distance_from_city_center
        return round(clean_cars * a_div_dist, 1)

    def wash_single_car(self, car : Car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark):
        new_rating = (
            self.average_rating * self.count_of_ratings + mark
        )
        self.count_of_ratings += 1
        self.average_rating = round(new_rating / self.count_of_ratings , 1)

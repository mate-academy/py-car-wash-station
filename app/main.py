class Car:

    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self, distance_from_city_center,
                 clean_power,
                 average_rating,
                 count_of_ratings):

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list):
        income = 0
        for car in car_list:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car):
        clean = (self.clean_power - car.clean_mark)
        a_rate_dist = (self.average_rating / self.distance_from_city_center)
        return round(clean * a_rate_dist * car.comfort_class, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
            return car

    def rate_service(self, s_rate):
        rate_sum = self.count_of_ratings * self.average_rating + s_rate
        self.count_of_ratings += 1
        self.average_rating = round(self.count_of_ratings / rate_sum, 1)
        return self

class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center,
                 clean_power,
                 average_rating,
                 count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars_classes):
        profit = 0
        for car in cars_classes:
            if car.clean_mark < self.clean_power:
                profit += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(profit, 1)

    def calculate_washing_price(self, car_class):
        clean_res = self.clean_power - car_class.clean_mark
        comfort_mult_clean = car_class.comfort_class * clean_res
        comfort_mult_rating = comfort_mult_clean * self.average_rating
        return round(comfort_mult_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, car):
        car.clean_mark = self.clean_power

    def rate_service(self, mark):
        sum_mean = self.average_rating * self.count_of_ratings + mark
        self.average_rating = round(sum_mean / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
        return self.average_rating

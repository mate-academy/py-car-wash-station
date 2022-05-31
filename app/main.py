class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center,
            clean_power, average_rating,
            count_of_ratings
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        car_wash_list = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                car_wash_list += \
                    (CarWashStation.calculate_washing_price(self, car))
                car.clean_mark = self.clean_power
        return car_wash_list

    def calculate_washing_price(self, car):
        result = car.comfort_class * (self.clean_power - car.clean_mark) * \
            (self.average_rating / self.distance_from_city_center)
        return round(result, 1)

    def wash_single_car(self, car):
        if self.clean_power >= car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate):
        self.average_rating = \
            round(
                (self.average_rating * self.count_of_ratings + rate) / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

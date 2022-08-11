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

    def serve_cars(self, cars):
        wash_single_car = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                wash_single_car += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
        return wash_single_car

    def calculate_washing_price(self, car):
        dif_ce = self.clean_power - car.clean_mark
        class_rate = car.comfort_class * self.average_rating
        price = round(class_rate * dif_ce / self.distance_from_city_center, 1)
        return price

    def wash_single_car(self, cars):
        for car in cars:
            if car.clean_mark < self.clean_power:
                car.clean_mark = self.clean_power

    def rate_service(self, number):
        all_marks = self.average_rating * self.count_of_ratings + number
        rate_service = all_marks / (self.count_of_ratings + 1)
        self.average_rating = round(rate_service, 1)
        self.count_of_ratings = self.count_of_ratings + 1

class Car:
    def __init__(self, comfort_class, clen_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clen_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        total = 0
        for car in cars:
            self.wash_single_car(car)
            total += round(self.calculate_washing_price(car), 1)
        return total

    def calculate_washing_price(self, Car):
        calculo = round(Car.comfort_class * (self.clean_power - Car.clean_mark) * self.average_rating / self.distance_from_city_center, 1)
        return calculo

    def wash_single_car(self, Car):
        if Car.clean_mark < self.clean_power:
            Car.clean_mark = self.clean_power
        else:
            pass


    def rate_service(self, num):
        self.average_rating += round((self.average_rating * self.count_of_ratings + num) / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

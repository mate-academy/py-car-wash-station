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

    def serve_cars(self, cars: list):
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car):
        clean_mark = self.clean_power - car.clean_mark
        mark = self.average_rating / self.distance_from_city_center
        return car.comfort_class * round(clean_mark * mark, 2)

    def wash_single_car(self, other):
        if self.clean_power > other.clean_mark:
            other.clean_mark = self.clean_power

    def rate_service(self, rate):
        avg = ((self.average_rating * self.count_of_ratings) + rate)
        self.count_of_ratings += 1
        self.average_rating = round(avg / self.count_of_ratings, 1)

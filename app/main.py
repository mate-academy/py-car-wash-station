class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power,
                 average_rating, count_of_ratings):
        self.distance = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car):
        diff_of_powers = self.clean_power - car.clean_mark
        cost = car.comfort_class * diff_of_powers * self.average_rating
        return round(cost / self.distance, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        return car

    def rate_service(self, rate):
        new_rate = (self.average_rating * self.count_of_ratings + rate)
        self.average_rating = round(new_rate / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

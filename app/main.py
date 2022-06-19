class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

    pass


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power,
                 average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        income = 0
        for car in cars:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car):
        price = 0
        if self.clean_power > car.clean_mark:
            dif = self.clean_power - car.clean_mark
            distance = self.distance_from_city_center
            price = (car.comfort_class * dif * self.average_rating / distance)
        return round(price, 1)

    def wash_single_car(self, car):
        if self.clean_power >= car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate):
        new_count = self.count_of_ratings + 1
        r = (self.average_rating * self.count_of_ratings + rate) / new_count
        self.average_rating = round(r, 1)
        self.count_of_ratings = new_count

    pass

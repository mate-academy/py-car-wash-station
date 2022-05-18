class Car:

    def __init__(self,
                 comfort_class,
                 clean_mark,
                 brand):
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

    def serve_cars(self, cars: list):
        cash = []
        for car in cars:
            if car.clean_mark < self.clean_power:
                cash.append(self.calculate_washing_price(car))
                self.wash_single_car(car)
        return sum(cash)

    def calculate_washing_price(self, one_car: Car):
        price = one_car.comfort_class * (
            self.clean_power - one_car.clean_mark) * \
            self.average_rating / \
            self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, single_car: Car):
        if single_car.clean_mark < self.clean_power:
            single_car.clean_mark = self.clean_power
        return single_car.clean_mark

    def rate_service(self, grade):
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + grade) / (
                self.count_of_ratings + 1),
            1)

        self.count_of_ratings = self.count_of_ratings + 1
        return self.average_rating

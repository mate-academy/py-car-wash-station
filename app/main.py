class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center,
            clean_power,
            average_rating,
            count_of_ratings
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        sum_of_price = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                sum_of_price += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(sum_of_price, 1)

    def calculate_washing_price(self, car: Car):
        possible_clean = self.clean_power - car.clean_mark
        before_dist = car.comfort_class * possible_clean * self.average_rating
        return before_dist / self.distance_from_city_center

    def wash_single_car(self, car: Car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int):
        sum_of_rates = self.average_rating * self.count_of_ratings + rate
        new_rating = sum_of_rates / (self.count_of_ratings + 1)
        self.average_rating = round(new_rating, 1)
        self.count_of_ratings += 1

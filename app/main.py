class Car:

    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str
    ):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(
        self,
        distance_from_city_center: int,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_mark = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car: Car):
        income = 0
        for i in car:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car):
        difference = self.clean_power - car.clean_mark
        multiplier = car.comfort_class * difference * self.average_rating
        return round(multiplier / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark):
        sum_count_rating = self.average_rating * self.count_of_ratings + mark
        self.count_of_ratings += 1
        self.average_rating = sum_count_rating / self.count_of_ratings
        self.average_rating = round(self.average_rating, 1)

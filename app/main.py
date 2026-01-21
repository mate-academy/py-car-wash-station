class Car:

    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        cost = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                cost += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return cost

    def calculate_washing_price(self, car):
        clean_work = self.clean_power - car.clean_mark
        cost_rating = self.average_rating / self.distance_from_city_center
        cost = car.comfort_class * clean_work * cost_rating
        return round(cost, 1)

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate):
        self.count_of_ratings += 1
        old_rating = self.average_rating * (self.count_of_ratings - 1) + rate
        self.average_rating = round(old_rating / self.count_of_ratings, 1)

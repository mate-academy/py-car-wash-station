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

    def calculate_washing_price(self, car):
        param = car.comfort_class * (self.clean_power - car.clean_mark)
        cost = param * self.average_rating / self.distance_from_city_center
        return round(cost, 1)

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
        return car

    def serve_cars(self, cars):
        profit = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                profit += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return profit

    def rate_service(self, mark):
        sum = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round((sum + mark) / self.count_of_ratings, 1)
        return self

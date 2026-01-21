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
        car_param = car.comfort_class * (self.clean_power - car.clean_mark)
        cost = car_param * self.average_rating / self.distance_from_city_center
        return round(cost, 1)

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
        return car

    def serve_cars(self, cars):
        incomes = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                incomes += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return incomes

    def rate_service(self, mark):
        start_rate_sum = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        new_rate = (start_rate_sum + mark) / self.count_of_ratings
        self.average_rating = round(new_rate, 1)
        return self

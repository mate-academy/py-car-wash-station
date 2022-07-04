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
        income = sum([
            self.calculate_washing_price(car) for car in cars
            if car.clean_mark < self.clean_power
        ])
        self.wash_single_car(cars)
        return round(income, 1)

    def calculate_washing_price(self, car: Car):
        washing_price = car.comfort_class *\
            (self.clean_power - car.clean_mark) *\
            self.average_rating / self.distance_from_city_center
        return round(washing_price, 1)

    def wash_single_car(self, cars: list):
        for car in cars:
            if car.clean_mark < self.clean_power:
                car.clean_mark = self.clean_power
        return cars

    def rate_service(self, new_rate: float):
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + new_rate)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
        return self.average_rating

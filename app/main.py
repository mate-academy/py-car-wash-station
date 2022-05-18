class Car:

    def __init__(self, comfort_class: int, clean_mark: int, car_brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = car_brand


class CarWashStation:

    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def income_calculation(self, car):
        result = self.calculate_washing_price(car)
        self.wash_single_car(car)
        return result

    def serve_cars(self, washes: list) -> float:
        return sum(self.income_calculation(car) for car in washes
                   if self.clean_power > car.clean_mark)

    def calculate_washing_price(self, car: Car):
        count_var = car.comfort_class * (self.clean_power - car.clean_mark)
        second_var = self.average_rating / self.distance_from_city_center
        return round(count_var * second_var, 1)

    def wash_single_car(self, car: Car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        return car

    def rate_service(self, vote: int):
        count_var = self.average_rating * self.count_of_ratings + vote
        vt = round(count_var / (self.count_of_ratings + 1), 1)
        self.average_rating = vt
        self.count_of_ratings += 1

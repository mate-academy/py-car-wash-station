class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self, distance_from_city_center: float, clean_power: int,
            average_rating: float, count_of_ratings: int
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: list) -> float:
        income = 0
        for car in car_list:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        clean_rate = self.clean_power - car.clean_mark
        rate = car.comfort_class * self.average_rating
        price = round(rate * clean_rate / self.distance_from_city_center, 1)
        return price

    def wash_single_car(self, car: Car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark):
        rating = self.average_rating * self.count_of_ratings + mark
        self.count_of_ratings += 1
        self.average_rating = round(rating / self.count_of_ratings, 1)

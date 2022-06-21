class Car:

    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, cars) -> float:
        dif = self.clean_power - cars.clean_mark
        wash_cost = cars.comfort_class * dif * self.\
            average_rating / self.distance_from_city_center
        return round(wash_cost, 1)

    def wash_single_car(self, cars):
        if self.clean_power > cars.clean_mark:
            cars.clean_mark = self.clean_power

    def rate_service(self, rating):
        self.average_rating = (self.average_rating * self.
                               count_of_ratings + rating
                               ) / (self.count_of_ratings + 1)
        self.average_rating = round(self.average_rating, 1)
        self.count_of_ratings += 1
        return self.average_rating

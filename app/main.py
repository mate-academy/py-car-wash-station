class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: float,
                 average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car):
        income = 0
        for c in car :
            if c.clean_mark <= self.clean_power :
                income += self.calculate_washing_price(c)
                c.clean_mark = self.clean_power
        return income

    def calculate_washing_price(self, car):
        wash_cost = round(car.comfort_class * (
            abs(car.clean_mark - self.clean_power)
        ) * self.average_rating / self.distance_from_city_center, 1)
        return wash_cost

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, mark):
        if mark:
            self.average_rating = round(
                (self.average_rating * self.count_of_ratings + mark) / (
                    self.count_of_ratings + 1), 1)
            self.count_of_ratings += 1

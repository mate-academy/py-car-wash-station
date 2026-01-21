class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        price = car.comfort_class * (
                    self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center
        return price

    def serve_cars(self, car_list: list) -> tuple:
        income = 0
        for car in car_list:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
        return round(income, 1)

    def wash_single_car(self, car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(cls, rate: float) -> float:
        if rate != 0:
            cls.count_of_ratings += 1
        sum_marks = cls.count_of_ratings * cls.average_rating
        sum_marks += rate
        cls.average_rating = sum_marks / cls.count_of_ratings
        return round(cls.average_rating, 1)


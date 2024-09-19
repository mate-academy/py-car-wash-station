import decimal


class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) \
            -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int,
                 average_rating: decimal, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> decimal:
        income_of_cars = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income_of_cars += self.calculate_washing_price(car)
                self.wash_single_car(car)
            else:
                continue
        return round(income_of_cars, 1)
    """method then return income of wash station and change clean_mark of car,
    if clean_mark less than clean_power of wash station"""

    def calculate_washing_price(self, car: type) -> decimal:
        wash_car_price = car.comfort_class * (
            self.clean_power - car.clean_mark) * self.average_rating \
            / self.distance_from_city_center
        return round(wash_car_price, 1)
    """method return washing price of single car"""

    def wash_single_car(self, car: type) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
    """method change clean_ mark of single car"""

    def rate_service(self, individual_rate: int) -> None:
        self.average_rating = round(((
            self.average_rating * self.count_of_ratings)
            + individual_rate) / (
            self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
    """method change rating of wash station and count of ratings"""

class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class: int = comfort_class
        self.clean_mark: int = clean_mark
        self.brand: str = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        price = car.comfort_class * (
            self.clean_power - car.clean_mark) * \
            self.average_rating / self.distance_from_city_center
        return round(price, 1)

    def serve_cars(self, cars: list[Car]) -> float:
        price = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price += self.wash_single_car(car)
        return price

    def wash_single_car(self, car: Car) -> float:
        price = self.calculate_washing_price(car)
        car.clean_mark = self.clean_power
        return price

    def rate_service(self, rating_point: float) -> None:
        old_count_of_ratings = self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = \
            (old_count_of_ratings / self.count_of_ratings) * \
            self.average_rating + \
            (1 / self.count_of_ratings) * rating_point
        self.average_rating = round(self.average_rating, 1)

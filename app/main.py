import typing


class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_rating: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_rating
        self.to_wash = 0

    def serve_cars(self, list_of_cars: list) -> float:
        return sum([self.calculate_washing_price(car) for car in list_of_cars
                    if self.wash_single_car(car)])

    def calculate_washing_price(self, other: typing.Any) -> float:
        return round(other.comfort_class * (
            self.clean_power - self.to_wash)
            * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, other: typing.Any) -> bool:
        if other.clean_mark < self.clean_power:
            self.to_wash = other.clean_mark
            other.clean_mark = self.clean_power

            return True

    def rate_service(self, single_rating: int) -> None:
        self.average_rating = round(
            (single_rating + self.average_rating * self.count_of_ratings)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

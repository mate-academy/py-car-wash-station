from typing import List


class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: float,
        brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: float,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        base_price = car.comfort_class * 10
        dirty_multiplier = 1 + (10 - car.clean_mark) / 10
        distance_price = self.distance_from_city_center * 0.5
        power_discount = min(self.clean_power / 100, 0.2)
        price = base_price * dirty_multiplier * (1 - power_discount)
        price += distance_price
        return round(price, 2)

    def wash_single_car(self, car: Car) -> float:
        price = self.calculate_washing_price(car)
        car.clean_mark = 10
        return price

    def serve_cars(self, cars: List[Car]) -> float:
        total = 0.0
        for car in cars:
            total += self.wash_single_car(car)
        return round(total, 2)

    def rate_service(self, new_rating: float) -> float:
        total = self.average_rating * self.count_of_ratings
        total += new_rating
        self.count_of_ratings += 1
        self.average_rating = total / self.count_of_ratings
        return round(self.average_rating, 2)

from typing import Any


class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        # 1. Валидация
        if not (1 <= comfort_class <= 7):
            raise ValueError("Comfort class must be between 1 and 7")
        if not (1 <= clean_mark <= 10):
            raise ValueError("Clean mark must be between 1 and 10")

        # 2. СОХРАНЕНИЕ (без этого будут ошибки AttributeError)
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        if not (1.0 <= distance_from_city_center <= 10.0):
            raise ValueError("Distance must be between 1.0 and 10.0")
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, сar: list) -> Any:
        income = 0.0
        for car in сar:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        clean_diff = self.clean_power - car.clean_mark
        coefficient = self.average_rating / self.distance_from_city_center
        price = (car.comfort_class * (clean_diff) * coefficient)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> Any:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        return car.clean_mark

    def rate_service(self, new_rate: int) -> Any:
        rating = self.average_rating * self.count_of_ratings + new_rate
        self.count_of_ratings += 1
        self.average_rating = round(rating / self.count_of_ratings, 1)
        return self.average_rating

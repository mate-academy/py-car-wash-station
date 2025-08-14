from typing import List


class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.brand = brand
        self.clean_mark = clean_mark
        self.comfort_class = comfort_class


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        total_price = 0.0

        for car in cars:
            if self.can_serve(car):
                price = self.calculate_washing_price(car)
                total_price += price
                self.wash_single_car(car)

        return round(total_price, 1)

    def calculate_washing_price(self, car: Car) -> float:
        cleanliness_difference = self.clean_power - car.clean_mark
        base_price = car.comfort_class * cleanliness_difference
        adjusted_price = (base_price * self.average_rating /
                         self.distance_from_city_center)

        return round(adjusted_price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        if not (1.0 <= rating <= 5.0):
            raise ValueError("Rating must be between 1.0 and 5.0")

        total_rating = self.average_rating * self.count_of_ratings
        new_total_rating = total_rating + rating
        new_count = self.count_of_ratings + 1

        self.count_of_ratings = new_count
        self.average_rating = round(new_total_rating / new_count, 1)

    def can_serve(self, car: Car) -> bool:
        return car.clean_mark < self.clean_power
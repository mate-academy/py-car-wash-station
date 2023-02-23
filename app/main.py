from typing import List


class Car:
    def __init__(self,
                 comfort_class: float,
                 clean_mark: float,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: float,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 1)

    def serve_cars(self, cars: List[Car]) -> float:
        income = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def rate_service(self, rating: float) -> None:
        new_count = self.count_of_ratings + 1
        new_avg = round((self.average_rating * self.count_of_ratings + rating)
                        / new_count, 1)
        self.count_of_ratings = new_count
        self.average_rating = new_avg

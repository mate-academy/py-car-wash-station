from typing import List


class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        if not (1 <= comfort_class <= 7):
            raise ValueError("comfort_class must be between 1 and 7")
        if not (1 <= clean_mark <= 10):
            raise ValueError("clean_mark must be between 1 and 10")
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int | float,
                 clean_power: int | float, average_rating: float,
                 count_of_ratings: int) -> None:
        if not (1.0 <= distance_from_city_center <= 10.0):
            raise ValueError("""distance_from_city_center must be
                             between 1.0 and 10.0""")
        if not (1.0 <= average_rating <= 5.0):
            raise ValueError("average_rating must be between 1.0 and 5.0")
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        total = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                total += price
                self.wash_single_car(car)
        return round(total, 1)

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int | float) -> None:
        total = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round((total + rating)
                                    / self.count_of_ratings, 1)

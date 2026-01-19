from __future__ import annotations


class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> Car:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: int,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> CarWashStation:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        incomes = 0
        for car in cars:
            income = self.wash_single_car(car)
            if income is not None:
                incomes += income
        return round(incomes, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = (car.comfort_class * (self.clean_power - car.clean_mark)
                 * self.average_rating / self.distance_from_city_center)

        return round(price, 1)

    def wash_single_car(self, car: Car) -> float:
        if self.clean_power > car.clean_mark:
            result = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return result

    def rate_service(self, score: int) -> None:
        score = self.average_rating * self.count_of_ratings + score
        self.count_of_ratings += 1
        self.average_rating = round(score / self.count_of_ratings, 1)

from typing import List


class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str,
                 ) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int,
                 ) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        dif = self.clean_power - car.clean_mark
        cost = (
            car.comfort_class * dif
            * self.average_rating / self.distance_from_city_center
        )
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> Car:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        return car

    def serve_cars(self, cars: List[Car]) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def rate_service(self, rating: int) -> None:
        total_rating = self.average_rating * self.count_of_ratings + rating
        new_average = total_rating / (self.count_of_ratings + 1)
        self.average_rating = round(new_average, 1)
        self.count_of_ratings += 1

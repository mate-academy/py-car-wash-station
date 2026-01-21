from typing import List


class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int
                 ) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        comfort_class = car.comfort_class
        clean_power = self.clean_power
        clean_mark = car.clean_mark
        average_rating = self.average_rating
        distance = self.distance_from_city_center
        cost = (comfort_class
                * (clean_power - clean_mark)
                * average_rating
                / distance)
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: List[Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def rate_service(self, rate: float) -> None:
        average_rating = self.average_rating
        count_of_raitings = self.count_of_ratings
        new_average = ((average_rating
                       * count_of_raitings + rate)
                       / (count_of_raitings + 1))
        self.average_rating = round(new_average, 1)
        self.count_of_ratings += 1

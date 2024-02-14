from typing import List


class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:

        self.distance_from_city = distance_from_city
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        income_counter = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                comfort_factor = car.comfort_class
                cleanliness_factor = self.clean_power - car.clean_mark
                rating_factor = self.average_rating
                distance_factor = 1 / self.distance_from_city
                count_factor_dist = rating_factor * distance_factor
                clean_and_comfort = comfort_factor * cleanliness_factor
                income_counter += (clean_and_comfort * count_factor_dist)
                car.clean_mark = self.clean_power
                self.wash_single_car(car)
        return round(income_counter, 1)

    def calculate_washing_price(self, car: Car) -> float:
        comfort_factor = car.comfort_class
        cleanliness_factor = self.clean_power - car.clean_mark
        rating_factor = self.average_rating
        distance_factor = 1 / self.distance_from_city
        general_factor = rating_factor / distance_factor
        washing_price = comfort_factor * cleanliness_factor * general_factor
        return round(washing_price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        self.count_of_ratings += 1
        multiply_res = self.count_of_ratings * self.average_rating
        total_ratings_sum = multiply_res + rate - self.average_rating
        result_count = total_ratings_sum / self.count_of_ratings
        self.average_rating = round(result_count, 1)

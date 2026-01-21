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
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars_list: List[Car]) -> float:
        """Washes list of cars and returns income."""
        return sum(self.wash_single_car(car) for car in cars_list)

    def rate_service(self, rating: int) -> None:
        """Adds new rating and calculates new average and updates count."""
        rates_sum = self.average_rating * self.count_of_ratings
        new_rates_sum = rates_sum + rating
        self.count_of_ratings += 1
        self.average_rating = round(new_rates_sum / self.count_of_ratings, 1)

    def wash_single_car(self, car: Car) -> float:
        """Cleans car if wash power is greater than clean mark."""
        price = 0
        if self.clean_power > car.clean_mark:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
        return price

    def calculate_washing_price(self, car: Car) -> float:
        """Calculates washing price of a car."""
        return round(
            (car.comfort_class
             * (self.clean_power - car.clean_mark)
             * self.average_rating
             / self.distance_from_city_center),
            1)

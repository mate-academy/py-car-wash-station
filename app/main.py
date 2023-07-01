from typing import List


class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(
            self,
            list_of_cars: List[Car]
    ) -> float:
        revenue = 0
        for car in list_of_cars:
            if self.clean_power > car.clean_mark:
                revenue += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(revenue, 1)

    def calculate_washing_price(
            self,
            car: Car
    ) -> float:
        if self.clean_power > car.clean_mark:
            clean_diff = self.clean_power - car.clean_mark
            multiple = car.comfort_class * clean_diff * self.average_rating
            wash_price = multiple / self.distance_from_city_center
            return round(wash_price, 1)

    def wash_single_car(
            self,
            car: Car
    ) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(
            self,
            rate: int
    ) -> None:
        total_rate = self.average_rating * self.count_of_ratings + rate
        raw_rating = total_rate / (self.count_of_ratings + 1)
        self.average_rating = round(raw_rating, 1)
        self.count_of_ratings += 1

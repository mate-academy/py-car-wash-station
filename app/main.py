from typing import List


class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:

        self.brand = brand

        if comfort_class < 1 or comfort_class > 7:
            raise ValueError("Comfort class must be between 1 and 7")
        self.comfort_class = comfort_class

        if clean_mark < 1 or clean_mark > 10:
            raise ValueError("Clean mark must be between 1 and 10")
        self.clean_mark = clean_mark


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:

        if not 1.0 <= distance_from_city_center <= 10.0:
            raise ValueError(
                "Distance from city center must be between 1.0 and 10.0")
        self.distance_from_city_center = distance_from_city_center

        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        total_income = 0
        cars_to_wash = []
        for car in cars:
            if car.clean_mark < self.clean_power:
                wash_cost = self.calculate_washing_price(car)
                total_income += wash_cost
                cars_to_wash.append(car)
        self.wash_multiple_cars(cars_to_wash)
        return round(
            total_income,
            1
        )

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class
                     * (self.clean_power
                        - car.clean_mark)
                     * self.average_rating
                     / self.distance_from_city_center,
                     1
                     )

    def wash_multiple_cars(self, cars: list) -> None:
        for car in cars:
            if self.clean_power > car.clean_mark:
                car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        if not 1.0 <= rating <= 5.0:
            raise ValueError("Rating must be between 1.0 and 5.0")

        self.average_rating = round((self.average_rating
                                     * self.count_of_ratings + rating)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

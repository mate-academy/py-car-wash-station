from typing import List


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int) -> None:
        self.distance_from_city_center = distance_from_city_center  # float
        self.clean_power = clean_power                              # int
        self.average_rating = 0.0                                   # float
        self.count_of_ratings = 0                                   # int

    def calculate_washing_price(self, car: Car) -> float:
        return round((car.comfort_class * 10) / self.distance_from_city_center, 2)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark += self.clean_power
        if car.clean_mark > 10:
            car.clean_mark = 10

    def serve_cars(self, cars: List[Car]) -> List[float]:
        prices: List[float] = []
        for car in cars:
            self.wash_single_car(car)
            price = self.calculate_washing_price(car)
            prices.append(price)
        return prices

    def rate_service(self, rating: int) -> None:
        total = self.average_rating * self.count_of_ratings + rating
        self.count_of_ratings += 1
        self.average_rating = round(total / self.count_of_ratings, 2)

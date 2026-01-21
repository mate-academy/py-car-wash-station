from typing import List


class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        if not (1 <= comfort_class <= 7
                and 1 <= clean_mark <= 10
                and isinstance(brand, str)):
            raise ValueError("Invalid arguments for Car.")
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int, ) -> None:
        if not (1.0 <= distance_from_city_center <= 10.0
                and 1 <= clean_power <= 10
                and 1.0 <= average_rating <= 5.0
                and isinstance(count_of_ratings, int)):
            raise ValueError("Invalid arguments for CarWashStation.")
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        return (car.comfort_class
                * (self.clean_power - car.clean_mark)
                * self.average_rating
                / self.distance_from_city_center)

    def wash_single_car(self, car: Car) -> float:
        if not isinstance(car, Car):
            raise ValueError("Invalid car object provided.")
        price = self.calculate_washing_price(car)
        car.clean_mark = self.clean_power
        return price

    def serve_cars(self, cars: List[Car]) -> float:
        return round(sum(
            self.wash_single_car(car)
            for car in cars
            if car.clean_mark < self.clean_power), 1, )

    def rate_service(self, rating: float) -> None:
        if not (1.0 <= rating <= 5.0):
            raise ValueError("Rating must be between 1.0 and 5.0.")
        total = self.average_rating * self.count_of_ratings + rating
        self.count_of_ratings += 1
        self.average_rating = round(total / self.count_of_ratings, 1)

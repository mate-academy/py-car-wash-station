from typing import List


class Car:
    def __init__(
            self,
            comfort_class: float,
            clean_mark: float,
            brand: str
    ) -> None:

        if not (1.0 <= comfort_class <= 7.0):
            raise ValueError("Comfort class must be between 1.0 and 7.0")
        if not (1.0 <= clean_mark <= 10.0):
            raise ValueError("Clean mark must be between 1.0 and 10.0")

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

    def __str__(self) -> str:
        return (f"{self.brand}, comfort class: {self.comfort_class}, "
                f"clean mark: {self.clean_mark}")


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: float,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        if not (1.0 <= distance_from_city_center <= 10.0):
            raise ValueError(
                "Distance from city center must be between 1.0 and 10.0"
            )
        if not (1.0 <= clean_power <= 10.0):
            raise ValueError("Clean power must be between 1.0 and 10.0")
        if not (1.0 <= average_rating <= 5.0):
            raise ValueError("Average rating must be between 1.0 and 5.0")
        if count_of_ratings < 0:
            raise ValueError("Count of ratings must be non-negative")

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: Car) -> bool:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
            return True
        return False

    def calculate_washing_price(self, car: Car) -> float:
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * (self.average_rating / self.distance_from_city_center)
        )
        price = max(price, 0.0)
        return round(price, 1)

    def serve_cars(self, cars_list: List[Car]) -> float:
        income = 0.0
        for car in cars_list:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                self.wash_single_car(car)
                income += price
        return round(income, 1)

    def rate_service(self, new_rating: float) -> float:
        if not (1.0 <= new_rating <= 5.0):
            raise ValueError("New rating must be between 1.0 and 5.0")
        total_ratings = self.count_of_ratings + 1
        new_avg = ((
            self.average_rating
            * self.count_of_ratings
            + new_rating)
            / total_ratings)
        self.average_rating = round(new_avg, 1)
        self.count_of_ratings = total_ratings
        return self.average_rating

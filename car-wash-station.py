from typing import List


class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = int(comfort_class)   # enforce int
        self.clean_mark = int(clean_mark)         # enforce int
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,                # must be int (same scale as Car.clean_mark)
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = float(distance_from_city_center)
        self.clean_power = int(clean_power)       # enforce int
        self.average_rating = round(float(average_rating), 1)
        self.count_of_ratings = int(count_of_ratings)

    def calculate_washing_price(self, car: Car) -> float:
        """
        Cost formula:
        comfort_class * (clean_power - car.clean_mark) * average_rating / distance
        Returns cost rounded to 1 decimal.
        If the car is already clean enough (clean_mark >= clean_power), cost is 0.
        """
        diff = self.clean_power - car.clean_mark
        if diff <= 0:
            return 0.0
        price = (
            car.comfort_class * diff * self.average_rating / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """Wash a single car to the station's clean_power if it is dirtier than that."""
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power     # always int

    def serve_cars(self, cars: List[Car]) -> float:
        """
        Wash all cars with clean_mark < clean_power.
        Sum their washing prices (each rounded to 1 decimal).
        Return total rounded to 1 decimal.
        """
        total = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total, 1)

    def rate_service(self, rate: float) -> None:
        """
        Add a new rating, updating both average_rating (rounded to 1 decimal)
        and count_of_ratings.
        """
        total_sum = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(total_sum / self.count_of_ratings, 1)

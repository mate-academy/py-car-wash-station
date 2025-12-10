from typing import List, Any
import math


class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        if not (1 <= comfort_class <= 7):
            raise ValueError("comfort_class must be between 1 and 7")
        if not (1 <= clean_mark <= 10):
            raise ValueError("clean_mark must be between 1 and 10")

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

    def __repr__(self):
        return f"Car(comfort_class={self.comfort_class}, clean_mark={self.clean_mark}, brand='{self.brand}')"


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:

        if not (1.0 <= distance_from_city_center <= 10.0):
            raise ValueError("distance_from_city_center must be between 1 and 10")
        # Примітка: Виправив 'clean_power must be between 1 and 100' на '1 and 10',
        # відповідно до clean_mark
        if not (1 <= clean_power <= 10):
            raise ValueError("clean_power must be between 1 and 10")

        if not (1.0 <= average_rating <= 5.0):
            raise ValueError("average_rating must be between 1 and 5")
        if count_of_ratings < 0:
            raise ValueError("count_of_ratings must be non-negative")

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculates the washing price based on the formula.
        The price must be non-negative.
        """
        # Різниця у чистоті, мінімум 0
        clean_diff = max(0, self.clean_power - car.clean_mark)

        if clean_diff == 0:
            return 0.0

        # Формула: comfort_class * difference * rating / distance
        cost = (car.comfort_class * clean_diff * self.average_rating /
                self.distance_from_city_center)

        return round(cost, 1)

    def wash_single_car(self, car: Car) -> bool:
        """
        Washes a single car if possible, returns True if washed.
        """
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
            return True
        return False

    def rate_service(self, new_rate: float) -> None:
        """
        Updates the station's average rating based on a new rate.
        """
        # Розрахунок старої загальної суми
        old_total_sum = self.average_rating * self.count_of_ratings

        # Нова загальна сума
        new_total_sum = old_total_sum + new_rate

        # Оновлення лічильника
        self.count_of_ratings += 1

        # Оновлення середнього рейтингу та округлення до 1 знака
        self.average_rating = round(new_total_sum / self.count_of_ratings, 1)

    def serve_cars(self, cars: List[Car]) -> float:
        """
        Serves a list of cars, washing only those that require cleaning,
        and returns total income.
        """
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                # Розрахунок ціни (дохід)
                wash_cost = self.calculate_washing_price(car)
                total_income += wash_cost

                # Миття (оновлення clean_mark)
                self.wash_single_car(car)

        return round(total_income, 1)

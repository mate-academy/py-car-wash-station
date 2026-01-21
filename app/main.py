from typing import List


class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class: int = comfort_class
        self.clean_mark: int = clean_mark
        self.brand: str = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: int,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center: int = distance_from_city_center
        self.clean_power: int = clean_power
        self.average_rating: float = average_rating
        self.count_of_ratings: int = count_of_ratings

    def serve_car(self, car: Car) -> float:
        """Обслуговує одну машину і повертає вартість або 0."""
        if car.comfort_class <= self.distance_from_city_center:
            cost: float = car.comfort_class * 11.2
            if car.clean_mark < self.clean_power:
                car.clean_mark = self.clean_power
            return cost
        return 0.0

    def serve_cars(self, cars: List[Car]) -> float:
        """Обслуговує список машин і повертає сумарний дохід."""
        total_income: float = 0.0
        for car in cars:
            total_income += self.serve_car(car)
        return total_income

    def rate_service(self, new_rating: int) -> None:
        """Оновлює середній рейтинг після нового відгуку."""
        total_score: float = self.average_rating * self.count_of_ratings
        total_score += new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_score / self.count_of_ratings, 1)

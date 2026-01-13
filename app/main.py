# app/main.py

class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, min_class: int, max_class: int, avg_rating: float,
                 num_ratings: int) -> None:
        self.min_class = min_class
        self.max_class = max_class
        self.avg_rating = avg_rating
        self.num_ratings = num_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0.0
        for car in cars:
            if self.min_class <= car.comfort_class <= self.max_class:
                price = self.calculate_washing_price(car)
                total_income += price
                if car.clean_mark < self.max_class:
                    car.clean_mark = self.max_class
        return total_income

    def calculate_washing_price(self, car: Car) -> float:
        # Простий приклад ціни: rating * comfort_class
        return self.avg_rating * car.comfort_class

    def rate_service(self, mark: int) -> None:
        total = self.avg_rating * self.num_ratings
        total += mark
        self.num_ratings += 1
        self.avg_rating = round(total / self.num_ratings, 1)

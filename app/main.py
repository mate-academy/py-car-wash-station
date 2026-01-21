# app/main.py

class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class  # клас комфорту
        self.clean_mark = clean_mark        # чистота авто
        self.brand = brand                  # бренд авто


class CarWashStation:
    def __init__(self, min_comfort_class: int, max_clean_mark: int, average_rating: float, count_of_ratings: int):
        self.min_comfort_class = min_comfort_class
        self.max_clean_mark = max_clean_mark
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        # Якщо автомобіль не відповідає вимогам, його не миють
        if car.comfort_class < self.min_comfort_class or car.clean_mark > self.max_clean_mark:
            return 0.0
        # Формула: ціна = comfort_class * (10 - clean_mark)
        price = car.comfort_class * (10 - car.clean_mark)
        return price

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        for car in cars:
            income += self.calculate_washing_price(car)
        return income

    def rate_service(self, mark: int):
        # оновлюємо середній рейтинг
        total = self.average_rating * self.count_of_ratings + mark
        self.count_of_ratings += 1
        self.average_rating = total / self.count_of_ratings

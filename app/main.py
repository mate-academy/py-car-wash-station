class Car:
    def __init__(self, size: int, clean_mark: int, model: str):
        self.size = size
        self.clean_mark = clean_mark
        self.model = model


class CarWashStation:
    def __init__(
        self,
        max_size: int,
        clear_power: int,
        average_rating: float,
        count_of_ratings: int
    ):
        self.max_size = max_size
        self.clear_power = clear_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        total_income = 0

        for car in cars:
            # Перевіряємо, чи можна мити авто
            if car.size > self.max_size or car.clean_mark > self.clear_power:
                continue

            # Оновлення чистоти машини
            if car.clean_mark < self.clear_power:
                car.clean_mark = self.clear_power

            # Ціна = size * average_rating
            cost = car.size * self.average_rating
            total_income += round(cost, 2)

        return round(total_income, 2)

    def rate_service(self, mark: int) -> None:
        # Формула з тестів (усереднення з округленням до 1 знаку)
        new_avg = (self.average_rating * self.count_of_ratings + mark) / (
            self.count_of_ratings + 1
        )
        self.count_of_ratings += 1
        self.average_rating = round(new_avg, 1)

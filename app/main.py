
class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        if not (1 <= comfort_class <= 7):
            raise ValueError("comfort_class має бути в діапазоні від 1 до 7.")
        if not (1 <= clean_mark <= 10):
            raise ValueError("clean_mark має бути в діапазоні від 1 до 10.")

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

    def __str__(self) -> str:
        return (f"Автомобіль {self.brand} "
                f"(Комфорт: {self.comfort_class}, Чистота: {self.clean_mark})")


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        # Перевірка діапазонів
        if not 1.0 <= distance_from_city_center <= 10.0:
            raise ValueError("distance_from_city_center має бути в"
                             " діапазоні від 1.0 до 10.0")
        if not 1 <= clean_power <= 10:
            raise ValueError("clean_power має бути в діапазоні від 1 до 10")
        if not 1.0 <= average_rating <= 5.0:
            raise ValueError("average_rating має бути в "
                             "діапазоні від 1.0 до 5.0")

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        clean_difference = self.clean_power - car.clean_mark
        short = self.average_rating / self.distance_from_city_center
        result = (car.comfort_class * clean_difference * short)
        return round(result, 1)

    def wash_single_car(self, car: Car) -> float:
        if self.clean_power > car.clean_mark:
            price = self.calculate_washing_price(car)
            # Миємо автомобіль
            car.clean_mark = self.clean_power
            return price
        else:
            return 0

    def rate_service(self, rating: int) -> None:
        if not 1 <= rating <= 5:
            raise ValueError("Рейтинг має бути в діапазоні від 1 до 5")

        current_rating_sum = self.average_rating * self.count_of_ratings
        new_rating = current_rating_sum + rating

        self.count_of_ratings += 1

        result = new_rating / self.count_of_ratings
        self.average_rating = round(result, 1)

    def serve_cars(self, cars: list[Car]) -> float:
        total_price = 0.0
        for car in cars:
            total_price += self.wash_single_car(car)
        return round(total_price, 1)

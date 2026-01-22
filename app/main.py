class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        if not (1 <= comfort_class <= 7):
            raise ValueError("comfort_class должен быть от 1 до 7.")
        if not (1 <= clean_mark <= 10):
            raise ValueError("clean_mark должен быть от 1 до 10.")
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        if not (1 <= distance_from_city_center <= 10):
            raise ValueError("должен быть от 1.0 до 10.0.")
        if not (1 <= clean_power <= 10):
            raise ValueError("clean_power должен быть от 1 до 10.")
        if not (1.0 <= average_rating <= 5.0):
            raise ValueError("average_rating должен быть от 1.0 до 5.0.")
        if count_of_ratings < 0:
            raise ValueError("count_of_ratings не может быть отрицательным.")

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """Метод для расчета стоимости мойки для одного автомобиля."""
        price = (car.comfort_class * (self.clean_power - car.
                                      clean_mark) * self.average_rating / self.
                 distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """Метод для мойки одного автомобиля."""
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        """Метод для мойки списка автомобилей и расчета общего дохода."""
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def rate_service(self, new_rating: float) -> None:
        """Метод для добавления нового рейтинга к станции."""
        if not (1.0 <= new_rating <= 5.0):
            raise ValueError("Рейтинг должен быть от 1.0 до 5.0.")
        total_rating = self.average_rating * self.count_of_ratings + new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)

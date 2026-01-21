class Car:
    def __init__(
            self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self, distance_from_city_center: float, clean_power: float,
            average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class * (self.clean_power - car.clean_mark) *
                     self.average_rating / self.distance_from_city_center, 1)

    def rate_service(self, rating: float) -> None:
        # Обчислюємо чисельник: сума всіх попередніх оцінок + нова оцінка
        new_total_sum = self.average_rating * self.count_of_ratings + rating
        # Обчислюємо новий середній рейтинг
        new_average = new_total_sum / (self.count_of_ratings + 1)
        # 1. Присвоюємо новий середній рейтинг, округлений до 1 знака
        self.average_rating = round(new_average, 1)
        # 2. Збільшуємо кількість оцінок
        self.count_of_ratings += 1

    def serve_cars(self, cars: list) -> float:
        car_served = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                car_served += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(car_served, 1)

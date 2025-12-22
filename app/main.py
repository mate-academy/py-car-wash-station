class Car:
    """Модель авто: клас комфорту, поточна чистота, бренд."""

    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class       # 1–7
        self.clean_mark = clean_mark             # 1–10
        self.brand = brand


class CarWashStation:
    """
    Мийка авто.
    distance_from_city_center: 1.0–10.0
    clean_power: цільова чистота, до якої миє ця станція (не всяка миє "до 10")
    average_rating: 1.0–5.0 (зберігаємо округленим до 1 знаку)
    count_of_ratings: кількість оцінок
    """

    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: Car) -> None:
        """Піднімає clean_mark авто до рівня clean_power, якщо він нижчий."""
        if car.clean_mark >= self.clean_power:
            return
        car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        """
        Рахує вартість миття БЕЗ фактичного миття.
        Формула: class * (clean_power - clean_mark) * rating / distance
        Повертає значення, округлене до 1 знаку.
        """
        missing_clean = self.clean_power - car.clean_mark
        base = car.comfort_class * missing_clean
        adjusted = base * self.average_rating
        price = adjusted / self.distance_from_city_center
        return round(price, 1)

    def serve_cars(self, cars: list[Car]) -> float:
        """
        Миє лише ті авто, у яких clean_mark < clean_power.
        Повертає загальний дохід, округлений до 1 знаку.
        """
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, rate: float) -> None:
        """Додає нову оцінку, оновлює середній рейтинг та лічильник оцінок."""
        total_score = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(total_score / self.count_of_ratings, 1)

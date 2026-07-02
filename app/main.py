class Car:
    def __init__(
        self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def rate_service(self, rate: int) -> None:
        total_rating_sum = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round(
            (total_rating_sum + rate) / self.count_of_ratings, 1
        )


bmw = Car(comfort_class=3, clean_mark=3, brand="BMW")
audi = Car(comfort_class=4, clean_mark=9, brand="Audi")
mercedes = Car(comfort_class=7, clean_mark=1, brand="Mercedes")

station = CarWashStation(
    distance_from_city_center=6,
    clean_power=8,
    average_rating=3.9,
    count_of_ratings=11,
)

print("Завдання 1")
income = station.serve_cars([bmw, audi, mercedes])
print(f"Загальний прибуток мийки: {income}")
print(f"Чистота BMW після мийки: {bmw.clean_mark}")
print(f"Чистота Audi після мийки: {audi.clean_mark}")
print(f"Чистота Mercedes після мийки: {mercedes.clean_mark}")

print("Завдання 2")
ford = Car(comfort_class=2, clean_mark=1, brand="Ford")
wash_cost = station.calculate_washing_price(ford)
print(f"Вартість миття для Ford: {wash_cost}")
print(f"Чистота Ford залишається базовою: {ford.clean_mark}")
print("-" * 40)

print("3 завдання")
print(
    f"Рейтинг до оцінки: {station.average_rating} "
    f"(Всього голосів: {station.count_of_ratings})"
)
station.rate_service(5)
print(
    f"Рейтинг після оцінки 5: {station.average_rating} "
    f"(Всього голосів: {station.count_of_ratings})"
)

class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.brand = brand
        self.comfort_class = comfort_class  # Спрацює сетер
        self.clean_mark = clean_mark  # Спрацює сетер

    @property
    def comfort_class(self) -> int:
        return self._comfort_class

    @comfort_class.setter
    def comfort_class(self, value: int) -> None:
        if not (1 <= value <= 7):
            raise ValueError("Клас комфорту має бути від 1 до 7")
        self._comfort_class = value

    @property
    def clean_mark(self) -> int:
        return self._clean_mark

    @clean_mark.setter
    def clean_mark(self, value: int) -> None:
        if not (1 <= value <= 10):
            raise ValueError("Знак чистоти автомобіля має бути від 1 до 10")
        self._clean_mark = value


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = float(distance_from_city_center)
        self.clean_power = int(clean_power)
        self.average_rating = round(float(average_rating), 1)
        self.count_of_ratings = int(count_of_ratings)

    def calculate_washing_price(self, car: Car) -> float:
        coefficient = car.comfort_class * (self.clean_power - car.clean_mark)
        price = (
            coefficient * self.average_rating / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                diff = self.clean_power - car.clean_mark
                exact_price = (
                    car.comfort_class
                    * diff
                    * self.average_rating
                    / self.distance_from_city_center
                )
                total_income += exact_price
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, new_rating: int) -> None:
        current_total_score = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        new_average = (
            current_total_score + new_rating
        ) / self.count_of_ratings
        self.average_rating = round(new_average, 1)

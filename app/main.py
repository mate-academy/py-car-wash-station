
class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str
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
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
        self.income = 0

    def calculate_washing_price(self, car: Car) -> float:
        first = car.comfort_class * (self.clean_power - car.clean_mark)
        price = first * self.average_rating / self.distance_from_city_center
        price = round(price, 1)
        return price

    def wash_single_car(self, car: Car) -> tuple[int, float]:
        self.income += self.calculate_washing_price(car)
        car.clean_mark = self.clean_power
        return car.clean_mark, self.income

    def serve_cars(self, cars: list[Car]) -> float:
        for car in cars:
            if car.clean_mark < self.clean_power:
                self.wash_single_car(car)
        self.income = round(self.income, 1)
        return self.income

    def rate_service(self, new_rating: int) -> tuple[float, int]:
        self.count_of_ratings += 1
        n_sum = self.average_rating * (self.count_of_ratings - 1) + new_rating
        self.average_rating = round(n_sum / self.count_of_ratings, 1)
        return self.average_rating, self.count_of_ratings

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

    def serve_cars(self, cars: list[Car]) -> float:
        return round(sum((self.calculate_washing_price(car),
                          self.wash_single_car(car))[0] for car in cars), 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = 0
        power_diff = self.clean_power - car.clean_mark
        formula = car.comfort_class * power_diff * self.average_rating
        if power_diff > 0:
            price += formula / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, single_rate: float) -> None:
        earlier_rate = self.average_rating * self.count_of_ratings
        total_rate = earlier_rate + single_rate
        avg_formula = total_rate / (self.count_of_ratings + 1)
        self.average_rating = round(avg_formula, 1)
        self.count_of_ratings += 1

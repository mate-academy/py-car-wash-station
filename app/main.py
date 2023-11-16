class Car():
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
            distance_from_city_center: int,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        diff = self.clean_power - car.clean_mark
        multi = car.comfort_class * diff * self.average_rating
        price = round(multi / self.distance_from_city_center, 1)
        return price

    def wash_single_car(self, car: list[Car]) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> float:
        total_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        sum_rat = total_rating + rating
        self.average_rating = round(sum_rat / self.count_of_ratings, 1)
        return self.average_rating

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

    def calculate_washing_price(self, car: Car) -> float:
        comfort_factor = car.comfort_class
        dirtiness_factor = self.clean_power - car.clean_mark
        rating_factor = self.average_rating
        distance_factor = self.distance_from_city_center

        price = (
            comfort_factor
            * dirtiness_factor
            * rating_factor
            / distance_factor
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def rate_service(self, new_rate: int) -> None:
        total_score = self.average_rating * self.count_of_ratings
        total_score += new_rate
        self.count_of_ratings += 1
        self.average_rating = round(
            total_score / self.count_of_ratings,
            1
        )

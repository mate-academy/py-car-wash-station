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
            clear_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clear_power = clear_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> int | float:
        all_income = []
        if cars:
            for car in cars:
                if self.clear_power > car.clean_mark:
                    all_income.append(self.calculate_washing_price(car))
                    self.wash_single_car(car)
            return round(sum(all_income), 1)
        return 0

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class
            * (self.clear_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center,
            1
        )

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clear_power

    def rate_service(self, rating: int) -> None:
        full_rating = self.average_rating * self.count_of_ratings
        full_rating += rating
        self.count_of_ratings += 1
        self.average_rating = round(full_rating / self.count_of_ratings, 1)

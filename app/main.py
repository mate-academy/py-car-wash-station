class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str = ""
    ) -> None:

        self.comfort_class = comfort_class if 1 <= comfort_class <= 7 else 1
        self.clean_mark = clean_mark if 1 <= clean_mark <= 10 else 1
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:

        self.distance_from_city_center = (
            distance_from_city_center
            if 1.0 <= distance_from_city_center <= 10.0
            else 1.0
        )
        self.clean_power = clean_power
        self.average_rating = (
            average_rating if 1.0 <= average_rating <= 5.0 else 1.0
        )
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center, 1
        )

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        old_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round(
            (old_rating + rating)
            / self.count_of_ratings, 1
        )

    def serve_cars(self, cars: list) -> float:
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

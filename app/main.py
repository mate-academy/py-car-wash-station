class Car:
    def __init__(
            self,
            comfort_class: int ,
            clean_mark: int,
            brand: str,
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

    def filter_cars_by_clean_mark(self, cars: list[Car]) -> list[Car]:
        return [
            car
            for car in cars
            if car.clean_mark < self.clean_power
        ]

    def serve_cars(self, cars: list[Car]) -> float | int:
        income = 0
        filtered_cars = self.filter_cars_by_clean_mark(cars)

        for car in filtered_cars:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)

        return income

    def calculate_washing_price(self, car: Car) -> float:
        dirtiness_level = self.clean_power - car.clean_mark
        washing_price = (
            car.comfort_class
            * dirtiness_level
            * self.average_rating
            / self.distance_from_city_center
        )

        return round(washing_price, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power \
            if self.clean_power > car.clean_mark \
            else car.clean_mark

    def rate_service(self, rate: int) -> None:
        current_rating = self.average_rating * self.count_of_ratings
        new_rating = current_rating + rate
        self.count_of_ratings += 1
        self.average_rating = round(
            new_rating / self.count_of_ratings,
            1,
        )

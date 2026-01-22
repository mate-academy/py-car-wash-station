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
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark <= self.clean_power:
                income += round(self.calculate_washing_price(car), 1)
                self.wash_single_car(car)
        return income

    def wash_single_car(self, car: object) -> None:
        car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        marks_to_clean = self.clean_power - car.clean_mark
        price_of_cleaning = (
            car.comfort_class
            * marks_to_clean
            * self.average_rating
            / self.distance_from_city_center
        )
        rounded_price_of_cleaning = round(price_of_cleaning, 1)
        return rounded_price_of_cleaning

    def rate_service(self, single_rate: int) -> None:
        new_amount_of_rate_points = (
            self.average_rating * self.count_of_ratings + single_rate
        )
        new_amount_of_ratings = self.count_of_ratings + 1
        new_rounded_average_rate = round(
            (new_amount_of_rate_points / new_amount_of_ratings), 1
        )
        self.average_rating = new_rounded_average_rate
        self.count_of_ratings += 1

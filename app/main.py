class Car:
    def __init__(
            self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self, distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    total_income: float = 0.0
    total_rating: int = 0

    def calculate_washing_price(self, obj_car: Car) -> float:
        return round(
            obj_car.comfort_class
            * (self.clean_power - obj_car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center,
            1,
        )

    def wash_single_car(self, obj_car: Car) -> float:
        price = self.calculate_washing_price(obj_car)

        if self.clean_power > obj_car.clean_mark:
            obj_car.clean_mark = self.clean_power

        return price

    def serve_cars(self, cars: list[Car]) -> float:
        current_income: float = 0.0

        for car in cars:
            if car.clean_mark < self.clean_power:
                current_income += self.wash_single_car(car)

        return round(current_income, 1)

    def rate_service(self, rate: int) -> None:
        total = self.average_rating * self.count_of_ratings
        total += rate
        self.count_of_ratings += 1
        self.average_rating = round(total / self.count_of_ratings, 1)

        return

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

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, model: Car) -> float:
        model_class = model.comfort_class
        power = self.clean_power
        is_car_dirty = model.clean_mark
        rating = self.average_rating
        distance = self.distance_from_city_center
        return round(
            model_class * (power - is_car_dirty) * rating / distance, 1
        )

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        avg_rating = self.average_rating
        count_ratings = self.count_of_ratings

        self.average_rating = round(
            (avg_rating * count_ratings + rate) / (count_ratings + 1), 1
        )
        self.count_of_ratings += 1

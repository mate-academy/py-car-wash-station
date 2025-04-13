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
        return sum([self.wash_single_car(car) for car in cars])

    def calculate_washing_price(self, car: Car) -> float:
        comform_class = car.comfort_class
        diff = self.clean_power - car.clean_mark
        rating = self.average_rating
        distance = self.distance_from_city_center
        price = round(comform_class * diff * rating / distance, 1)
        return price

    def wash_single_car(self, car: Car) -> float:
        if self.clean_power <= car.clean_mark:
            return 0
        single_car_income = self.calculate_washing_price(car)
        car.clean_mark = self.clean_power
        return single_car_income

    def rate_service(self, mark: int) -> None:
        future_rating_count = self.count_of_ratings + 1
        expression = self.average_rating * self.count_of_ratings + mark
        self.average_rating = round(
            expression / future_rating_count,
            1
        )
        self.count_of_ratings = future_rating_count

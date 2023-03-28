class Car:
    def __init__(
            self, comfort_class: int, clean_mark: int, brand: str
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

    def can_wash_car(self, car: Car) -> bool:
        return car.clean_mark < self.clean_power

    def wash_single_car(self, car: Car) -> None:
        if self.can_wash_car(car):
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        if self.can_wash_car(car):
            diff = (self.clean_power - car.clean_mark)
            return round(
                (
                    (
                        car.comfort_class * diff * self.average_rating
                    ) / self.distance_from_city_center
                ), 1
            )
        return 0.0

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return income

    def rate_service(self, rate: int) -> None:
        sum_rate = (self.average_rating * self.count_of_ratings) + rate
        self.count_of_ratings = self.count_of_ratings + 1
        self.average_rating = round((sum_rate / self.count_of_ratings), 1)

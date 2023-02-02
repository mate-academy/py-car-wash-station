# v.1.0
class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars_car_instances: list) -> float:
        costs = 0
        for car in cars_car_instances:
            if car.clean_mark < self.clean_power:
                costs += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return costs

    def calculate_washing_price(self, car: Car) -> float:

        return round(
            car.comfort_class * (
                self.clean_power - car.clean_mark
            ) * self.average_rating / self.distance_from_city_center, 1
        )

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        s_a_r = self.average_rating
        s_c_r = self.count_of_ratings
        self.average_rating = round((
            s_a_r * s_c_r + rate) / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

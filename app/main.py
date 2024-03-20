class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: int,
            clean_power: int,
            average_rating: int,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> int:
        total_cost = 0
        for car in cars:
            if self.wash_single_car(car):
                total_cost += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
        return total_cost

    def wash_single_car(self, car: Car) -> bool:
        if self.clean_power > car.clean_mark:
            return True
        return False

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * (self.average_rating / self.distance_from_city_center),
            1
        )

    def rate_service(self, rate: int) -> None:
        too_brilliant_rating_system = [self.average_rating] \
            * self.count_of_ratings
        too_brilliant_rating_system.append(rate)
        self.count_of_ratings += 1
        self.average_rating = round(
            sum(too_brilliant_rating_system)
            / len(too_brilliant_rating_system),
            1
        )

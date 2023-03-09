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
        count_of_ratings: float,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def rate_service(self, num: int) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + num)
            / (self.count_of_ratings + 1),
            1,
        )
        self.count_of_ratings += 1

    def calculate_washing_price(self, car: Car) -> float:
        cost = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
        ) / self.distance_from_city_center
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> int:
        car.clean_mark = self.clean_power
        return car.clean_mark

    def serve_cars(self, cars: list) -> float:
        cost_sum = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                cost_sum += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return cost_sum

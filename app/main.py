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

    def calculate_washing_price(self, self_car: Car) -> float:
        res = self_car.comfort_class * (self.clean_power - self_car.clean_mark)
        res *= self.average_rating / self.distance_from_city_center
        return round(res, 1)

    def wash_single_car(self, self_car: Car) -> float:
        if self_car.clean_mark <= self.clean_power:
            res = self.calculate_washing_price(self_car)
            self_car.clean_mark = self.clean_power
            return res
        return 0

    def serve_cars(self, cars: list) -> float:
        costs = 0
        for i in cars:
            costs += self.wash_single_car(i)
        return costs

    def rate_service(self, rate: int) -> None:
        average = self.average_rating * self.count_of_ratings + rate
        new_average = average / (self.count_of_ratings + 1)

        self.average_rating = round(new_average, 1)
        self.count_of_ratings += 1

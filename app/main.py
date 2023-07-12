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
            distance_from_city_center: int,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center, 1)

    def serve_cars(self, cars_list: list) -> float:
        res = 0
        for car in cars_list:
            if car.clean_mark < self.clean_power:
                res += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return res

    def wash_single_car(self, car: tuple) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark: float) -> None:
        self.count_of_ratings += 1
        total_rating = self.average_rating * (self.count_of_ratings - 1)
        self.average_rating = round(
            (total_rating + mark) / self.count_of_ratings, 1
        )
        round(self.count_of_ratings, 1)

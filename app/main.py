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
            distance_from_city_center: int,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.count_of_ratings = count_of_ratings
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.distance_from_city_center = distance_from_city_center

    def calculate_washing_price(self, car: Car) -> float:
        price = round(
            (car.comfort_class * (self.clean_power - car.clean_mark)
             * (self.average_rating / self.distance_from_city_center)), 1)
        return price

    def wash_single_car(self, car: Car) -> bool:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> float:
        income_of_wash_station = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income_of_wash_station += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income_of_wash_station

    def rate_service(self, rate: float) -> None:
        sum_rate = (self.average_rating * self.count_of_ratings) + rate
        self.average_rating = round(
            (sum_rate / (self.count_of_ratings + 1)), 1
        )
        self.count_of_ratings += 1

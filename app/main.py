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
        pre_serve_cars = [
            car for car in cars
            if self.is_possible_wash_car(car)
        ]
        income = sum(
            [
                self.calculate_washing_price(car)
                for car in pre_serve_cars
            ]
        )
        for car in pre_serve_cars:
            self.wash_single_car(car)
        return round(income, ndigits=1)

    def calculate_washing_price(self, car: Car) -> float:
        clean_dif = self.clean_power - car.clean_mark
        station_rate = self.average_rating / self.distance_from_city_center
        cost = car.comfort_class * clean_dif * station_rate
        return cost

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def is_possible_wash_car(self, car: Car) -> bool:
        return True if car.clean_mark < self.clean_power else False

    def rate_service(self, rate: int) -> None:
        last_sum = self.average_rating * self.count_of_ratings
        self.average_rating = (last_sum + rate) / (self.count_of_ratings + 1)
        self.average_rating = round(self.average_rating, 1)
        self.count_of_ratings += 1

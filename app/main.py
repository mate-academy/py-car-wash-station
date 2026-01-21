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

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark > self.clean_power:
            return 0
        comfort_price = (car.comfort_class
                         * (self.clean_power - car.clean_mark)
                         * self.average_rating)
        price = comfort_price / self.distance_from_city_center
        return round(price, 1)

    def serve_cars(self, cars: list) -> int:
        total = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total, 1)

    def wash_single_car(self, car: Car) -> int:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
        return car.clean_mark

    def rate_service(self, rating: float) -> float:
        self.count_of_ratings += 1
        total_rating = (self.average_rating * (self.count_of_ratings - 1)
                        + rating)
        self.average_rating = round(total_rating / self.count_of_ratings, 1)
        return self.average_rating

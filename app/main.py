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
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        money = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                money += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return money

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        power_mark_diff = self.clean_power - car.clean_mark
        rating_div_distance = (
            self.average_rating / self.distance_from_city_center
        )
        price = round(
            car.comfort_class * power_mark_diff * rating_div_distance, 1
        )

        return price

    def rate_service(self, rating: float) -> float:
        self.count_of_ratings += 1
        count = self.count_of_ratings
        self.average_rating = round(
            ((count - 1) * self.average_rating + rating) / count, 1
        )

        return self.average_rating

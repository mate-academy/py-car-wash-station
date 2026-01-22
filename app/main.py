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
        self.average_rating = round(
            average_rating, 1
        )
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list["Car"]) -> float:
        price = 0.0
        for car in cars:
            difference = self.clean_power - car.clean_mark
            if difference > 0:
                price += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(price, 1)

    def calculate_washing_price(self, car: "Car") -> float:
        difference = self.clean_power - car.clean_mark
        if difference <= 0:
            return 0.0
        raw_cost = car.comfort_class * difference * self.average_rating
        return round(raw_cost / self.distance_from_city_center, 1)

    def wash_single_car(self, car: "Car") -> None:
        difference = self.clean_power - car.clean_mark
        if difference > 0:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        old_avg = self.average_rating
        old_cnt = self.count_of_ratings

        new_cnt = old_cnt + 1
        new_avg = (old_avg * old_cnt + rating) / new_cnt

        self.count_of_ratings = new_cnt
        self.average_rating = round(new_avg, 1)

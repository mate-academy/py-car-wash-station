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
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        price_for_car = round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center,
            1,
        )
        return price_for_car

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power <= car.clean_mark:
            return
        car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> float:
        total_income = 0.0
        for car in cars:
            if self.clean_power > car.clean_mark:
                price_for_car = self.calculate_washing_price(car)
                self.wash_single_car(car)
                total_income += price_for_car
        return total_income

    def rate_service(self, rating: float) -> None:
        current_total = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round(
            (current_total + rating) / self.count_of_ratings, 1
        )

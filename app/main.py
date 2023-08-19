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
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        between_power_and_mark = self.clean_power - car.clean_mark
        car_class_multiply_between = car.comfort_class * between_power_and_mark
        multiply_and_ratings = car_class_multiply_between * self.average_rating
        return round(multiply_and_ratings / self.distance_from_city_center, 1)

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        average = self.average_rating * self.count_of_ratings
        new_rating = (average + rating) / (self.count_of_ratings + 1)
        self.average_rating = round(new_rating, 1)
        self.count_of_ratings += 1

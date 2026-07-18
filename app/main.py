class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
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
        power_diff = self.clean_power - car.clean_mark
        rating_dist_ratio = (
            self.average_rating / self.distance_from_city_center
        )
        washing_price = (
            car.comfort_class
            * power_diff
            * rating_dist_ratio
        )
        return round(washing_price, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> float:
        general_income = 0.0
        for car in cars:
            if self.clean_power > car.clean_mark:
                washing_price_of_current_car = (
                    self.calculate_washing_price(car)
                )
                general_income += washing_price_of_current_car
                self.wash_single_car(car)
        return round(general_income, 1)

    def rate_service(self, grade: int) -> None:
        total_rating_points = (
            self.average_rating * self.count_of_ratings + grade
        )
        new_average_rating = total_rating_points / (self.count_of_ratings + 1)
        self.count_of_ratings += 1
        self.average_rating = round(new_average_rating, 1)

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

    def serve_cars(self, car_list: list) -> int | float:
        income = 0
        for car in car_list:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> int | float:
        if car.clean_mark >= self.clean_power:
            return 0
        clean_power_difference = self.clean_power - car.clean_mark
        rating_to_distance_ratio = (self.average_rating
                                    / self.distance_from_city_center)
        result = round(
            car.comfort_class
            * clean_power_difference
            * rating_to_distance_ratio,
            1
        )
        return result

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int | float) -> None:
        total_rating = self.count_of_ratings * self.average_rating + rating
        self.average_rating = round(
            total_rating
            / (self.count_of_ratings + 1),
            1
        )
        self.count_of_ratings += 1

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

    def serve_cars(self, car_list: list[Car]) -> float:
        total_income = 0
        for car in car_list:
            if car.clean_mark < self.clean_power:
                cost = self.calculate_washing_price(car)
                total_income += cost
                self.wash_single_car(car)
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class
                     * (self.clean_power - car.clean_mark)
                     * self.average_rating
                     / self.distance_from_city_center,
                     1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        new_total_ratings = (self.average_rating
                             * self.count_of_ratings
                             + rating)
        self.count_of_ratings += 1
        self.average_rating =\
            round(new_total_ratings / self.count_of_ratings, 1)

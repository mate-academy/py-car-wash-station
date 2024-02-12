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
            distance_from_city_to_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_to_center = distance_from_city_to_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: [Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return income

    def calculate_washing_price(self, car: Car) -> float:
        power_for_car = self.clean_power - car.clean_mark
        cost = (car.comfort_class
                * power_for_car
                * self.average_rating
                / self.distance_from_city_to_center)
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> None:
        # works without condition, cause I check above
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark: int) -> None:
        all_ratings = self.average_rating * self.count_of_ratings
        updated_rating = all_ratings + mark
        self.count_of_ratings += 1
        self.average_rating = round(updated_rating / self.count_of_ratings, 1)

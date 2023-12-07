
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
            average_rating: float = None,
            count_of_ratings: float = None
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: list[Car]) -> float:
        return round(car.comfort_class
                     * (self.clean_power
                        - car.clean_mark)
                     * self.average_rating
                     / self.distance_from_city_center
                     , 1)

    def wash_single_car(self, car: list[Car]) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        self.average_rating = round(
            (self.average_rating
             * self.count_of_ratings + rating)
            / (self.count_of_ratings + 1)
            , 1)
        self.count_of_ratings += 1

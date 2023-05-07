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
            average_rating: (int, float),
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        return (
            round((car.comfort_class
                   * (self.clean_power - car.clean_mark)
                   * self.average_rating / self.distance_from_city_center), 1)
            if self.clean_power > car.clean_mark
            else 0
        )

    # def wash_single_car(self, car: Car) -> None:

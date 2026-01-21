class Car:
    def __init__(
            self, comfort_class: int, clean_mark: int, brand: str) -> None:
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

    def serve_cars(self, car_list: list[Car]) -> float:
        income = 0

        for auto in car_list:
            if auto.clean_mark < self.clean_power:
                income += self.wash_single_car(auto)

        return round(income, 1)

    def calculate_washing_price(self, auto: Car) -> float:
        if self.distance_from_city_center == 0:
            return round(
                auto.comfort_class * (self.clean_power - auto.clean_mark)
                * self.average_rating, 2)

        return round(
            auto.comfort_class * (self.clean_power - auto.clean_mark)
            * self.average_rating / self.distance_from_city_center , 2)

    def wash_single_car(self, auto: Car) -> float:
        if self.clean_power > auto.clean_mark:
            result = self.calculate_washing_price(auto)
            auto.clean_mark = self.clean_power
            return result

        return 0

    def rate_service(self, rate: float) -> None:
        self.average_rating = round(
            (rate + self.average_rating * self.count_of_ratings)
            / (self.count_of_ratings + 1), 1
        )
        self.count_of_ratings += 1

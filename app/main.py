class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_auto: list) -> float:
        count_cash = 0
        for auto in list_auto:
            if auto.clean_mark < self.clean_power:
                count_cash += self.calculate_washing_price(auto)
                self.wash_single_car(auto)
        return round(count_cash, 1)

    def calculate_washing_price(self,
                                auto: str) -> float:
        return round((auto.comfort_class * (self.clean_power - auto.clean_mark)
                      * self.average_rating
                      / self.distance_from_city_center), 1)

    def wash_single_car(self, auto: str) -> str:
        if self.clean_power > auto.clean_mark:
            auto.clean_mark = self.clean_power

    def rate_service(self, new_rate: float) -> None:
        self.average_rating = round((self.average_rating
                                    * self.count_of_ratings + new_rate)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.clean_mark = None
        self.comfort_class = None
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list, wash_station: list) -> None:
        for car in cars:
            if car.clean_mark < car.clean_power:
                income = wash_station.serve_cars([cars])
                return income

    def calculate_washing_price(self) -> None:
        return self.comfort_class * ((self.clean_power - self.clean_mark)
                                     * (self.average_rating
                                        / self.distance_from_city_center))

    def wash_single_car(self, wash_station: list, car: list) -> None:
        if wash_station.clean_power > car.clean_mark:
            self.clean_mark = wash_station.clean_power

    def rate_service(self, wash_station: list) -> None:
        return wash_station.rate_service()

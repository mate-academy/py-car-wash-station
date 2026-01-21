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

    def serve_cars(self, list_of_cars: list[Car]) -> float:
        income = 0
        for car in list_of_cars:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        washing_value = self.clean_power - car.clean_mark
        station_status = self.average_rating / self.distance_from_city_center
        washing_price = car.comfort_class * washing_value * station_status
        return round(washing_price, 1)

    def wash_single_car(self, single_car: Car) -> None:
        single_car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        sum_of_all_rates = (self.average_rating * self.count_of_ratings + rate)
        average_rating = sum_of_all_rates / (self.count_of_ratings + 1)
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings += 1

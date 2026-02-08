class Car:
    def __init__(
            self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: int,
            clean_power: int,
            average_rating: int,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: list) -> int:
        result = 0
        for car in list_of_cars:
            if car.clean_mark < self.clean_power:
                result += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(result, 1)

    def calculate_washing_price(self, auto: Car) -> None:
        difference = self.clean_power - auto.clean_mark
        distance_factor = self.average_rating / self.distance_from_city_center
        return round(auto.comfort_class * difference * distance_factor, 1)

    def wash_single_car(self, auto: Car) -> None:
        if auto.clean_mark < self.clean_power:
            auto.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        total_rate = rate + self.average_rating * self.count_of_ratings
        self.average_rating = round(
            (total_rate) / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
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
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, other):
        income = 0
        for vehicle in other:
            if self.clean_power > vehicle.clean_mark:
                income += self.calculate_washing_price(vehicle)
                vehicle.clean_mark = self.clean_power
        return income

    def calculate_washing_price(self, other):
        return round(
            other.comfort_class * (
                self.clean_power - other.clean_mark
            ) * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, other):
        if self.clean_power > other.clean_mark:
            return self.clean_power

    def rate_service(self, other):
        sum_of_ratings = self.average_rating * self.count_of_ratings
        sum_of_ratings += other
        self.count_of_ratings += 1
        self.average_rating = round(
            (sum_of_ratings / self.count_of_ratings), 1)
        return self.average_rating

from decimal import Decimal


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
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        difference = max(self.clean_power - car.clean_mark, 0)
        return round(
            car.comfort_class * difference
            * self.average_rating
            / self.distance_from_city_center, 1
        )

    def serve_cars(self, many_car: list) -> float:
        result = 0
        for one_car in many_car:
            if one_car.clean_mark < self.clean_power:
                result += self.calculate_washing_price(one_car)
                self.wash_single_car(one_car)
        return result

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        total_rating = \
            Decimal(self.average_rating) * self.count_of_ratings + \
            Decimal(rating)
        self.count_of_ratings += 1
        self.average_rating = float(total_rating / self.count_of_ratings)
        self.average_rating = round(self.average_rating, 1)

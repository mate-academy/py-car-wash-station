from typing import List


class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str
    ) -> None:
        if not (1 <= comfort_class <= 7):
            raise ValueError(
                "comfort_class must be between 1 and 7"
            )

        if not (1 <= clean_mark <= 10):
            raise ValueError(
                "clean_mark must be between 1 and 10"
            )

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
        if not (1.0 <= distance_from_city_center <= 10.0):
            raise ValueError(
                "distance_from_city_center must be between 1.0 and 10.0"
            )

        if not (1.0 <= average_rating <= 5.0):
            raise ValueError(
                "average_rating must be between 1.0 and 5.0"
            )

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        base_price = car.comfort_class * 10
        distance_penalty = (10.0 - self.distance_from_city_center) * 2
        price = base_price + distance_penalty
        return round(price, 2)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: List[Car]) -> List[float]:
        prices = []
        for car in cars:
            price = self.calculate_washing_price(car)
            self.wash_single_car(car)
            prices.append(price)
        return prices

    def rate_service(self, rating: int) -> None:
        if not (1 <= rating <= 5):
            raise ValueError(
                "rating must be between 1 and 5"
            )

        total_rating = self.average_rating * self.count_of_ratings + rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)


def calculate_comfort_score(
    comfort_class: int,
    distance_from_city_center: float
) -> float:
    if not (1 <= comfort_class <= 7):
        raise ValueError(
            "comfort_class must be between 1 and 7"
        )

    if not (1.0 <= distance_from_city_center <= 10.0):
        raise ValueError(
            "distance_from_city_center must be between 1.0 and 10.0"
        )

    base_score = comfort_class * 10
    distance_penalty = (10.0 - distance_from_city_center) * 2
    final_score = base_score + distance_penalty
    return round(final_score, 2)

from typing import Optional, List


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

    def serve_cars(self, cars: List[Optional["Car"]]) -> int:
        """
        method, that takes a list of Car's,
        washes only cars with clean_mark < clean_power of wash station
        and returns income of CarWashStation for serving this list of Car's,
        rounded to 1 decimal:
        """

        total_cost = 0

        for car in cars:
            total_cost += self.wash_single_car(car)

        return total_cost

    def wash_single_car(self, car: Optional["Car"]) -> float:
        """
        method, that washes a single car,
        so it should have clean_mark equals wash station's clean_power,
        if wash_station.clean_power is greater than car.clean_mark;
        """
        price = self.calculate_washing_price(car)
        if price:
            car.clean_mark = self.clean_power
            return price

        return round(0, 1)

    def calculate_washing_price(self, car: Optional["Car"]) -> float:
        """
        method, that calculates cost for a single car wash,
        cost is calculated as: car's comfort class * difference
        between wash station's clean power and
        car's clean mark * car wash station rating / car wash station
        distance to the center of the city,
        returns number rounded to 1 decimal;
        """
        if car.clean_mark < self.clean_power:
            return round(
                car.comfort_class * (self.clean_power - car.clean_mark)
                * (self.average_rating / self.distance_from_city_center)
                , 1
            )
        return 0

    def rate_service(self, rate: int) -> None:
        """
        method that adds a single rate to the wash station,
        and based on this single rate average_rating
        and count_of_ratings should be changed:
        """
        total_rating = (self.average_rating * self.count_of_ratings) + rate
        self.average_rating = round(
            total_rating / (self.count_of_ratings + 1)
            , 1
        )
        self.count_of_ratings += 1

from typing import List


class Car:
    def __init__(
            self, comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        """Here we are initializing the car class."""
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
        """
        Here we are initializing the car wash station class.
        Take in mind that distance_from_city can't be 0,
        it's minimum 1.0 and maximum 10.0.
        """
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        """
        Here we're calculating income from any count of car.
        To calculate income, we're using 'calculate_washing_price' method.
        """
        income = 0.0
        if self.clean_power <= 0:
            return income
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        """
        Here we're calculating income from washing car.
        Also, we're rounding result to one decimal.
        """
        distance = self.distance_from_city_center
        rate_distance = self.average_rating / distance if distance != 0 else 1
        power_mark = self.clean_power - car.clean_mark
        income = car.comfort_class * power_mark * rate_distance
        return round(income, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        Here we're change clean_mark
        """
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> float:
        """
        Here we're taking new rate and calculating new average rating.
        After calculating we're rounding our new rate to one decimal.
        """
        previous_sum_of_rate = self.average_rating * self.count_of_ratings
        new_sum_of_rate = previous_sum_of_rate + rate
        new_avg_rate = round(new_sum_of_rate / (self.count_of_ratings + 1), 1)
        self.average_rating = new_avg_rate
        self.count_of_ratings += 1
        return new_avg_rate

class Car:
    def __init__(
            self, comfort_class: int,
            clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: int | float,
            clean_power: int,
            average_rating: int | float,
            count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        """
        The method, that takes a list of cars, washes only cars with
        clean_mark < clean_power of  wash station and returns income of
        CarWashStation for serving this list of cars,
        rounded to 1 decimal.
        """
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        """
        The method, that calculates cost for a single car wash,
        cost is calculated as: car's comfort class
        * difference between wash station's clean power and
        car's clean mark * car wash station rating / car wash station
        distance to the center of the city.
        """
        comfort_factor = car.comfort_class
        clean_difference = self.clean_power - car.clean_mark
        rating_factor = self.average_rating / self.distance_from_city_center

        price = comfort_factor * clean_difference * rating_factor
        return round(price, 1)

    def wash_single_car(self, car: Car) -> int:
        """
        The method, that washes a single car, so it should have clean_mark
        equals wash station's clean_power,
        if wash_station.clean_power is greater than car.clean_mark.
        """
        car.clean_mark = self.clean_power

    def rate_service(self, new_rating: int | float) -> None:
        """
        The method that adds a single rate to the wash station,
        and based on this single rate average_rating and
        count_of_ratings should be changed.
        """
        total_rating = (self.average_rating * self.count_of_ratings)
        total_rating += new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating
                                    / self.count_of_ratings, 1)

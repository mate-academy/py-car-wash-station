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
            distance_from_city_center: int | float,
            clean_power: int,
            average_rating: int | float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        """
        Washes cars and returns the income for serving them.
        :param cars: a list of Car instances
        :return: income - a number rounded to 1 decimal
        """
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                car.clean_mark = self.wash_single_car(car)
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculates the cost for a single car wash.
        :param car: a Car instance
        :return: the washing price - a number rounded to 1 decimal
        """
        clean_power_clean_mark_difference = self.clean_power - car.clean_mark
        rating_divided_by_distance = (self.average_rating
                                      / self.distance_from_city_center)
        return round(
            car.comfort_class * clean_power_clean_mark_difference
            * rating_divided_by_distance, 1
        )

    def wash_single_car(self, car: Car) -> int:
        """
        Washes a single car.
        :param car: a Car instance
        :return: car's clean mark value
        """
        car.clean_mark = self.clean_power
        return car.clean_mark

    def rate_service(self, new_rate_score: int | float) -> None:
        """
        Adds a single rate to the wash station.
        :param new_rate_score: a rate mark - an int or float number
        """
        current_count_of_rating = self.count_of_ratings
        current_rate_score = self.average_rating * current_count_of_rating
        self.count_of_ratings += 1
        self.average_rating = round(
            (current_rate_score + new_rate_score) / self.count_of_ratings, 1
        )

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

    def serve_cars(self, cars: list) -> float:
        """
        Washes each car in the given list and returns the total income
        :param cars:
        :return:
        """
        income = 0

        for car in cars:
            income += self.wash_single_car(car)

        return income

    def wash_single_car(self, car: Car) -> float:
        """
        Washes a single car if its clean mark is lower than clean power of
        the washing station
        :param car:
        :return:
        """
        single_income = 0

        if car.clean_mark < self.clean_power:
            single_income += self.calculate_washing_price(car)
            car.clean_mark = self.clean_power

        return single_income

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculates washing price depending on a comfort class of a car,
        a difference between clean power of a washing station and a clean mark
        of a car, and a rating to distance to center ratio
        :param car:
        :return:
        """
        difference_between_clean_power_and_clear_mark = (self.clean_power
                                                         - car.clean_mark)
        rating_to_distance_to_center = (self.average_rating
                                        / self.distance_from_city_center)

        return round(car.comfort_class
                     * difference_between_clean_power_and_clear_mark
                     * rating_to_distance_to_center, 1)

    def rate_service(self, rating: float) -> None:
        """
        Recalculates the average_rating attribute according to the given rating
        :param rating:
        """
        self.count_of_ratings += 1
        self.average_rating = round((self.average_rating
                                     * (self.count_of_ratings - 1)
                                     + rating)
                                    / self.count_of_ratings, 1)

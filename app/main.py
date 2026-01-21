class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
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
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculates cost: (comfort_class * diff_clean * rating) / distance
        """
        diff = self.clean_power - car.clean_mark
        cost = (
            car.comfort_class * diff * self.average_rating
        ) / self.distance_from_city_center
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        Washes a car to the station's clean_power level if the car is dirtier.
        """
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        """
        Processes a list of cars.
        Only washes cars where car.clean_mark < station.clean_power.
        Returns total income rounded to 1 decimal.
        """
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                # Calculate price BEFORE washing to get the correct difference
                price = self.calculate_washing_price(car)
                income += price
                # Perform the wash
                self.wash_single_car(car)

        return round(income, 1)

    def rate_service(self, new_rate: float) -> None:
        """
        Updates average rating and count of ratings based on a new input rate.
        """
        total_rating_score = self.average_rating * self.count_of_ratings
        total_rating_score += new_rate
        self.count_of_ratings += 1
        self.average_rating = round(
            total_rating_score / self.count_of_ratings, 1
        )

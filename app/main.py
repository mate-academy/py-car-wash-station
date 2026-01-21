class Car:
    """Represents a car with comfort class, cleanliness, and brand."""

    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str,
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    """Represents a car wash station with cleaning and rating logic."""

    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculate washing price for a single car.

        Formula:
            comfort_class * (clean_power - clean_mark)
            * average_rating / distance_from_city_center
        Returns price rounded to 1 decimal.
        """
        if car.clean_mark >= self.clean_power:
            return 0.0

        diff = self.clean_power - car.clean_mark
        price = (
            car.comfort_class * diff * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        Wash a single car.

        Updates car.clean_mark to station's clean_power if the station can
        clean better. Does not return any value.
        """
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        """
        Serve a list of cars.

        For each car with clean_mark < clean_power:
          1. Calculate price using calculate_washing_price().
          2. Wash the car.
          3. Add price to total income.
        Returns total income rounded to 1 decimal.
        """
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                self.wash_single_car(car)
                total_income += price
        return round(total_income, 1)

    def rate_service(self, rate: int) -> None:
        """
        Add a single rate to the station and update its average rating.

        Average rating is rounded to 1 decimal.
        """
        total = self.average_rating * self.count_of_ratings
        total += rate
        self.count_of_ratings += 1
        self.average_rating = round(total / self.count_of_ratings, 1)

class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        comfort_class: int,
        clear_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.comfort_class = comfort_class
        self.clear_power = clear_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    # --- INTERNAL LOGIC ---

    def wash_single_car(self, car: Car) -> None:
        """Update clean_mark if the car can be washed."""
        if car.clean_mark < self.clear_power:
            car.clean_mark = self.clear_power

    def calculate_washing_price(self, car: Car) -> float:
        """
        Price is zero if the car cannot be washed.
        Otherwise:
            price = car.comfort_class * self.average_rating
        This method *must not* change car.clean_mark.
        """
        if car.clean_mark >= self.clear_power:
            return 0

        return car.comfort_class * self.average_rating

    # --- MAIN PUBLIC METHOD ---

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0

        for car in cars:
            # price must be computed BEFORE washing!
            total_income += self.calculate_washing_price(car)

            # method must be called (test checks patch)
            self.wash_single_car(car)

        return round(total_income, 1)

    # --- RATING SYSTEM ---

    def rate_service(self, mark: int) -> None:
        """
        New average:
            new_avg = (old_avg * old_n + mark) / (old_n + 1)
        """
        new_total = self.average_rating * self.count_of_ratings + mark
        self.count_of_ratings += 1
        self.average_rating = round(new_total / self.count_of_ratings, 1)

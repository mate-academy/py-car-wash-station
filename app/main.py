class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings
        self.income = 0.0

    def serve_cars(self, cars: list) -> float:
        """Wash all eligible cars and calculate total income."""
        total_income = 0
        for car in cars:
            total_income += self.wash_single_car(car)  # call wash_single_car
        # self.income += total_income
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        """Calculate washing price."""
        delta = self.clean_power - car.clean_mark
        base = car.comfort_class * delta
        res = base * self.average_rating / self.distance_from_city_center
        return round(res, 1)

    def wash_single_car(self, car: Car) -> None or int:
        """Wash a single car and return income from washing it."""
        if car.clean_mark < self.clean_power:
            # Income formula (can be your custom calculation)
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price
        return 0

    def rate_service(self, rate: int) -> None:

        """
           Add a new customer rating and update the average rating.
        """
        res = (((self.average_rating * self.count_of_ratings) + rate)
               / (self.count_of_ratings + 1))

        self.average_rating = round(res, 1)
        self.count_of_ratings = self.count_of_ratings + 1

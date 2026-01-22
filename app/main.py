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
            clean_power: float,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        """
        Takes a list of Car's, washes only cars
        with clean_mark < clean_power of wash station
        and returns income of CarWashStation for serving this list of Car's,
        rounded to 1 decimal
        """
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                print(f"***I can clean {car.brand}***")
                self.wash_single_car(car)
        return round(total_income, 1)

    def calculate_washing_price(self, car: any) -> float:
        """
        Calculates cost for a single car wash, cost is calculated as:
        car's comfort class * difference between wash station's
        clean power and car's clean mark * car wash station rating
        / car wash station distance to the center of the city
        """
        washing_price = round(
            car.comfort_class * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center, 1)
        print(f"Price washing {car.brand}: {washing_price}")
        return washing_price

    def wash_single_car(self, car: str) -> None:
        """
        Washes a single car. If the station's clean_power is greater than
        the car's clean_mark, then clean_mark is equal to clean_power.
        """
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        """
        Updates the average rating and the number of people
        after receiving a new rating.
        """
        self.average_rating = round(
            (self.count_of_ratings * self.average_rating + rating)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
        print(f"New rating station: {self.average_rating}"
              f"({self.count_of_ratings}people)")

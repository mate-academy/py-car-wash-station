class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        """
        Initializes the Car object with its properties.

        Args:
            comfort_class: The comfort class of the car (1-7).
            clean_mark: The current cleanness mark of the car (1-10).
            brand: The brand of the car.
        """
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float, count_of_ratings: int) -> None:
        """
        Initializes the CarWashStation object with its properties.

        Args:
            distance_from_city_center: Distance from the city center (1.0-10.0).
            clean_power: The cleanness mark the station can wash to.
            average_rating: The average rating of the station (1.0-5.0).
            count_of_ratings: The number of people who rated the station.
        """
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calculates the washing price for a single car.

        The price is calculated as: comfort_class * (clean_power - clean_mark) * average_rating / distance.

        Args:
            car: An instance of the Car class.

        Returns:
            The calculated washing price, rounded to 1 decimal place.
        """
        if self.clean_power <= car.clean_mark:
            return 0.0

        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        Washes a single car, updating its clean_mark if it's below the station's clean_power.

        Args:
            car: An instance of the Car class.
        """
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        """
        Washes a list of cars and returns the total income.
        Only cars with a clean_mark below the station's clean_power are washed.

        Args:
            cars: A list of Car instances.

        Returns:
            The total income from washing the cars, rounded to 1 decimal place.
        """
        total_income = 0.0
        for car in cars:
            if self.clean_power > car.clean_mark:
                price = self.calculate_washing_price(car)
                self.wash_single_car(car)
                total_income += price
        return round(total_income, 1)

    def rate_service(self, rate: int) -> None:
        """
        Adds a new rating to the wash station and updates the average rating.

        Args:
            rate: A single new rating (integer).
        """
        current_total_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        new_total_rating = current_total_rating + rate
        self.average_rating = round(new_total_rating / self.count_of_ratings, 1)

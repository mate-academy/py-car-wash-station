class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.brand = brand
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:

        if not (1 <= distance_from_city_center <= 10):
            raise ValueError("Distance from city center "
                             "must be between 1 and 10.")
        if not (1 <= average_rating <= 5):
            raise ValueError("Average rating must be between 1 and 5.")

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: list[Car]) -> float:
        """Maintains a list of cars and returns the
        total cost of the car wash."""
        if isinstance(list_of_cars, Car):
            return self.wash_single_car(list_of_cars)
        return round(sum(self.wash_single_car(car) for car in list_of_cars), 1)

    def calculate_washing_price(self, car: Car) -> float:
        """Calculates the cost of washing for a specific car."""
        result = (car.comfort_class * (self.clean_power - car.clean_mark)
                  * self.average_rating / self.distance_from_city_center)
        return round(result, 1)

    def wash_single_car(self, car: Car) -> float:
        """Washes one car if the power of the station is greater
         than the current cleanliness of the car."""
        if self.clean_power > car.clean_mark:
            result = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return result
        return 0.0

    def rate_service(self, rating: float) -> None:
        """Updates the station's average rating after a new rating."""
        self.average_rating = round((self.average_rating
                                     * self.count_of_ratings + rating)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

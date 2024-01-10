class Car:
    def __init__(
            self, comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

    def __str__(self) -> str:
        return (
            f"Car(comfort_class = {self.comfort_class}) "
            f"clean_mark = {self.clean_mark} "
            f"brand = {self.brand})"
        )


class CarWashStation:
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

    def serve_cars(self, cars: list[Car]) -> float:
        price = 0

        for car in cars:
            if car.clean_mark < self.clean_power:
                price += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return price

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center,
            1,
        )

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, mark: int) -> None:
        sum_of_points = self.average_rating * self.count_of_ratings
        sum_of_points += mark

        self.count_of_ratings += 1
        self.average_rating = round(sum_of_points / self.count_of_ratings, 1)

    def __str__(self) -> str:
        return (
            f"CarWashStation("
            f"distance_from_city_center = {self.distance_from_city_center}) "
            f"clean_power = {self.clean_power} "
            f"average_rating = {self.average_rating} "
            f"count_of_ratings = {self.count_of_ratings})"
        )

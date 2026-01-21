class Car:
    def __init__(
        self, comfort_class: int,
        clean_mark: int,
        brand: str
    ) -> None:
        if not (1 <= comfort_class <= 7):
            raise ValueError("Comfort class must be between 1 and 7")
        if not (1 <= clean_mark <= 10):
            raise ValueError("Clean mark must be between 1 and 10")

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
        if not (1.0 <= distance_from_city_center <= 10.0):
            raise ValueError(
                "distance_from_city_center must be between 1.0 and 10.0"
            )
        if not (1 <= clean_power <= 10):
            raise ValueError("clean_power must be between 1 and 10")
        if not (1.0 <= average_rating <= 5.0):
            raise ValueError("average_rating must be between 1.0 and 5.0")

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0

        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                self.wash_single_car(car)
                total_income += price
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float | int:
        if self.clean_power <= car.clean_mark:
            return 0

        posible_cleanliness_improvment_mark = self.clean_power - car.clean_mark

        washing_price = (
            car.comfort_class
            * posible_cleanliness_improvment_mark
            * self.average_rating
            / self.distance_from_city_center
        )

        return round(washing_price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rating: float) -> None:
        if not (1.0 <= new_rating <= 5.0):
            raise ValueError("new_rating must be between 1.0 and 5.0")

        total_rating_sum = (
            self.count_of_ratings
            * self.average_rating
            + new_rating
        )
        new_count_of_ratings = self.count_of_ratings + 1
        new_average_rating = (total_rating_sum / new_count_of_ratings)

        self.average_rating = round(new_average_rating, 1)
        self.count_of_ratings = new_count_of_ratings

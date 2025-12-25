class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str,
    ) -> None:
        assert 1 <= comfort_class <= 7, "comfort_class must be in range [1, 7]"
        self.comfort_class = comfort_class

        assert 1 <= clean_mark <= 10, "clean_mark must be in range [1, 10]"
        self.clean_mark = clean_mark

        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        assert (
            1.0 <= distance_from_city_center <= 10.0
        ), "distance_from_city_center must be in range [1.0, 10.0]"
        self.distance_from_city_center = distance_from_city_center

        assert 1 <= clean_power <= 10, "clean_power must be in range [1, 10]"
        self.clean_power = clean_power

        assert (
            1.0 <= average_rating <= 5.0
        ), "average_rating must be in range [1.0, 5.0]"
        self.average_rating = average_rating

        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            result = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return result
        return 0.0

    def serve_cars(self, cars: list[Car]) -> float:
        return sum(self.wash_single_car(car) for car in cars)

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center,
            1,
        )

    def rate_service(self, mark: int) -> None:
        total_rating = self.average_rating * self.count_of_ratings + mark
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)

class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str
    ) -> None:

        if not (1 <= comfort_class <= 7):
            raise ValueError(
                "comfort_class must be in range 1..7"
            )

        if not (1 <= clean_mark <= 10):
            raise ValueError(
                "clean_mark must be in range 1..10"
            )

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
                "distance_from_city_center must be in range 1.0..10.0"
            )

        if not (1.0 <= average_rating <= 5.0):
            raise ValueError(
                "average_rating must be in range 1.0..5.0"
            )

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def _calculate_washing_price_raw(self, car: Car) -> float:
        return (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )

    def calculate_washing_price(self, car: Car) -> float:
        return round(self._calculate_washing_price_raw(car), 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> float:
        amount = 0

        for car in cars:
            if car.clean_mark < self.clean_power:
                amount += self._calculate_washing_price_raw(car)
                self.wash_single_car(car)

        return round(amount, 1)

    def rate_service(self, num: int) -> None:
        old_total = self.average_rating * self.count_of_ratings
        new_total = old_total + num
        new_count = self.count_of_ratings + 1

        self.average_rating = round(new_total / new_count, 1)
        self.count_of_ratings = new_count

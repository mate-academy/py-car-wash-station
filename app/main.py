class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        if not (1 <= comfort_class <= 7):
            raise ValueError("should be from 1 to 7")
        self.comfort_class = comfort_class
        if not (1 <= clean_mark <= 10):
            raise ValueError("should be from 1 to 10")
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        if not (1 <= distance_from_city_center <= 10):
            raise ValueError("should be from 1.0 to 10.0")
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        if not (1 <= round(average_rating, 1) <= 5):
            raise ValueError("should be from 1.0 to 5.0")
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float | None:
        return round(
                    (car.comfort_class * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center), 1
        )

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float | None:
        carwash_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                carwash_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return carwash_income

    def rate_service(self, new_rate: float) -> None:
        self.average_rating = round((self.average_rating
                                    * self.count_of_ratings + new_rate)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

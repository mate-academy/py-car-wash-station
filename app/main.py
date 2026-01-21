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

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center,
            1
        )

    def wash_single_car(self, car: Car) -> float:
        return self.calculate_washing_price(car)

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.wash_single_car(car)
                car.clean_mark = self.clean_power
        return round(income, 1)

    def rate_service(self, mark: int) -> None:
        if 1 <= mark <= 5:
            all_marks_sum = (
                self.average_rating * self.count_of_ratings + mark
            )
            self.count_of_ratings += 1
            self.average_rating = round(
                all_marks_sum / self.count_of_ratings, 1
            )

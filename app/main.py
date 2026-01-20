class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
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
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> int:
        total_income = 0
        for car in cars:
            if isinstance(car.clean_mark, int) and isinstance(self.clean_power, int):
                if car.clean_mark < self.clean_power:
                    income = car.comfort_class * 1.25
                    total_income += income
                    car.clean_mark = self.clean_power
            else:
                print("Incorrect data type")
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        total_price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(total_price, 1)

    def wash_single_car(self, car: Car) -> None:
        if isinstance(car.clean_mark, int) and isinstance(self.clean_power, int):
            if car.clean_mark < self.clean_power:
                car.clean_mark = self.clean_power
        else:
            print("Incorrect data type")

    def rate_service(self, rating: int) -> None:
        if not (1 <= rating <= 5):
            print("Rating must be between 1 and 5.")
            return

        self.count_of_ratings += 1
        self.average_rating = round(
            (
                (self.average_rating * (self.count_of_ratings - 1))
                + rating
            ) / self.count_of_ratings,
            1,
        )

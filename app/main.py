class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str
    ) -> None:
        if comfort_class < 1 or comfort_class > 7:
            raise ValueError("comfort_class must be between 1 and 7 inclusive")

        if clean_mark < 1 or clean_mark > 10:
            raise ValueError("clean_mark must be between 1 and 10 inclusive")

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
                "distance_from_city_center must be between "
                "1.0 and 10.0 inclusive"
            )

        if not (1 <= clean_power <= 10):
            raise ValueError("clean_power must be between 1 and 10 inclusive")

        if not (1.0 <= average_rating <= 5.0):
            raise ValueError(
                "average_rating must be between "
                "1.0 and 5.0 inclusive"
            )

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        price = (car.comfort_class * (self.clean_power - car.clean_mark)
                 * self.average_rating / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def rate_service(self, rating: float) -> None:
        total_rating = self.average_rating * self.count_of_ratings + rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)

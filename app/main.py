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
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: list[Car]) -> float:
        total_cost = 0
        for car in list_of_cars:
            if self.clean_power >= car.clean_mark:
                total_cost += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_cost, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            (car.comfort_class * (self.clean_power - car.clean_mark)
             * self.average_rating / self.distance_from_city_center), 1
        )

    def rate_service(self, customer_service_rating: int) -> None:
        self.average_rating = round(
            (self.count_of_ratings * self.average_rating
             + customer_service_rating)
            / (self.count_of_ratings + 1), 1
        )
        self.count_of_ratings = self.count_of_ratings + 1

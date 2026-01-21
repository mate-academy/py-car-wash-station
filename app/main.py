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
            distance_from_city_centre: float,
            clean_power: float,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_centre = distance_from_city_centre
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income = (
                    car.comfort_class
                    * (self.clean_power - car.clean_mark)
                    * (self.average_rating / self.distance_from_city_centre)
                )
                self.wash_single_car(car)
                total_income += income
        return round(total_income, 1)

    def calculate_washing_price(self, car: float) -> float:
        if car.clean_mark < self.clean_power:
            cost = (car.comfort_class
                    * (self.clean_power - car.clean_mark)
                    * (self.average_rating / self.distance_from_city_centre))
            return round(cost, 1)
        return 0.0

    def wash_single_car(self, car: float) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rate)
            / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

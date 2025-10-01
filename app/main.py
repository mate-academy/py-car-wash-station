class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:
        self.comfort_class: int = comfort_class
        self.clean_mark: int = clean_mark
        self.brand: str = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center: float = distance_from_city_center
        self.clean_power: int = clean_power
        self.average_rating: float = average_rating
        self.count_of_ratings: int = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        total_sale: float = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_sale += self.wash_single_car(car)
        return total_sale

    def calculate_washing_price(self, car: Car) -> float:
        cost: float = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> float:
        price = self.calculate_washing_price(car)
        car.clean_mark = self.clean_power
        return price

    def rate_service(self, single_rate: float) -> None:
        previous_total_rate: float = (
            self.average_rating * self.count_of_ratings
        )
        self.count_of_ratings += 1
        new_total_rate: float = previous_total_rate + single_rate
        self.average_rating = round(new_total_rate / self.count_of_ratings, 1)

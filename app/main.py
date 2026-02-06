class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class: int = comfort_class
        self.clean_mark: int = clean_mark
        self.brand: str = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center: float = distance_from_city_center
        self.clean_power: int = clean_power
        self.average_rating: float = average_rating
        self.count_of_ratings: int = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        price: float = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            / self.distance_from_city_center
            * self.average_rating
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            price: float = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price
        return 0.0

    def serve_cars(self, cars: list[Car]) -> float:
        income: float = 0.0
        for car in cars:
            income += self.wash_single_car(car)
        return round(income, 1)

    def rate_service(self, rating: float) -> float:
        total_rating: float = self.average_rating * self.count_of_ratings
        total_rating += rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)
        return self.average_rating

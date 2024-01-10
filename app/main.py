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
            distance_from_city_center: float = 1,
            clean_power: int = 0,
            average_rating: float = 0.0,
            count_of_ratings: int = 0
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        filtered_cars = [
            car
            for car in cars
            if car.clean_mark <= self.clean_power
        ]
        income = sum(
            [
                self.calculate_washing_price(car)
                for car in filtered_cars
            ]
        )
        for car in filtered_cars:
            self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = round(
            car.comfort_class * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center,
            1
        )
        return price

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark <= self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, mark: int) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + mark)
            / (self.count_of_ratings + 1),
            1
        )
        self.count_of_ratings += 1

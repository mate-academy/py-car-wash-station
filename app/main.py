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
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = sum([car.clean_mark
                      for car in cars
                      if car.clean_mark < self.clean_power])
        return round(income, 1)

    def calculate_washing_price(self, cars: list[Car]) -> float:
        income = 0
        washable_cars = [car for car in cars if self.wash_single_car(car)]

        for car in washable_cars:
            income += self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
        return income

    def wash_single_car(self, car: Car) -> bool:
        if self.clean_power > car.clean_mark:
            return True
        else:
            return False

    def rate_service(self, new_rating: int) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + new_rating)
            / (self.count_of_ratings + 1), 1
        )
        self.count_of_ratings += 1

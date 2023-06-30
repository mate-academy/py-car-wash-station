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

    def calculate_washing_price(self, car: Car) -> float:
        amount_of_work = self.clean_power - car.clean_mark
        multiply = car.comfort_class * amount_of_work * self.average_rating
        return round(multiply / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> bool:
        return self.clean_power >= car.clean_mark

    def rate_service(self, number: float) -> None:
        part1 = self.average_rating * self.count_of_ratings + number
        part2 = self.count_of_ratings + 1

        new_rating = round(part1 / part2, 1)
        self.average_rating = new_rating
        self.count_of_ratings += 1

    def serve_cars(self, cars: list[Car]) -> None:
        income = 0

        for car in cars:
            if self.wash_single_car(car):
                income += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power

        return income

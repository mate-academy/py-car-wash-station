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

    def serve_cars(self, cars: list[Car]) -> int:
        final_price = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                final_price += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return final_price

    def calculate_washing_price(self, car: Car) -> float:
        math_part1 = self.clean_power - car.clean_mark
        math_part2 = self.average_rating / self.distance_from_city_center
        math_part3 = car.comfort_class * math_part1 * math_part2
        return round(math_part3, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rate: int) -> None:
        math_part1 = self.average_rating * self.count_of_ratings
        math_part2 = math_part1 + new_rate
        math_part3 = self.count_of_ratings + 1
        math_part4 = math_part2 / math_part3
        self.average_rating = round(math_part4, 1)
        self.count_of_ratings += 1

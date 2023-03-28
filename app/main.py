class Car:

    def __init__(self, comfort_clss: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_clss
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(
            self, distance: float, power: float, rating: float, count: int
    ) -> None:
        self.distance_from_city_center = distance
        self.clean_power = power
        self.average_rating = rating
        self.count_of_ratings = count

    def calculate_washing_price(self, car: Car) -> float:
        difference = self.clean_power - car.clean_mark
        upper_part = car.comfort_class * difference * self.average_rating
        return round(upper_part / self.distance_from_city_center, 1)

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        sum_of_rates = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(sum_of_rates / self.count_of_ratings, 1)

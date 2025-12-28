class Car:
    def __init__(
            self, comfort_class: int, clean_mark: float, brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self, distance_from_city_center: float, clean_power: float,
            average_rating: float, count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            clean_difference = self.clean_power - car.clean_mark
            price = (
                    (car.comfort_class * clean_difference
                     * self.average_rating) / self.distance_from_city_center)
            return round(price, 1)
        return 0

    def wash_single_car(self, car: Car) -> float:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
            return self.calculate_washing_price(car)
        return 0

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return income

    def rate_service(self, rating: int) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)

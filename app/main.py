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
        clean = self.clean_power - car.clean_mark
        dist_rating = self.average_rating / self.distance_from_city_center
        return round(car.comfort_class * clean * dist_rating, 1)

    def rate_service(self, rating: float) -> None:
        self.count_of_ratings += 1
        total_rating = self.average_rating * (self.count_of_ratings - 1)
        temp_rating = (total_rating + rating) / self.count_of_ratings
        self.average_rating = round(temp_rating, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power >= car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> int | float:
        income = 0
        for car in cars:
            if car.clean_mark <= self.clean_power:
                washing_price = self.calculate_washing_price(car)
                income += round(washing_price, 1)
                self.wash_single_car(car)

        return income

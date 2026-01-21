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

    def serve_cars(self, cars: list[Car]) -> float:
        washing_price = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                washing_price += self.wash_single_car(car)
        return round(washing_price, 1)

    def calculate_washing_price(self, car: Car) -> float:
        difference_of_clean = self.clean_power - car.clean_mark
        price = car.comfort_class * difference_of_clean * self.average_rating
        return round(price / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            washing_price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return round(washing_price, 1)
        return 0

    def rate_service(self, rating: int) -> None:
        overall_rating = self.average_rating * self.count_of_ratings + rating
        self.count_of_ratings += 1
        self.average_rating = round(overall_rating / self.count_of_ratings, 1)

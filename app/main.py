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

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                income += price
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: object) -> float:
        difference = self.clean_power - car.clean_mark
        score = car.comfort_class * difference * self.average_rating
        result = score / self.distance_from_city_center
        return round(result, 1)

    def wash_single_car(self, car: object) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, note: int) -> None:
        self.count_of_ratings += 1
        self.average_rating = round(
            ((note + self.average_rating * (self.count_of_ratings - 1))
             / self.count_of_ratings),
            1
        )

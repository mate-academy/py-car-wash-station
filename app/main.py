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
            distance_from_city_center: int | float,
            clean_power: int | float,
            average_rating: float = 0.0,
            count_of_ratings: float = 0
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = car.comfort_class * (self.clean_power - car.clean_mark)
        calc_price = price * self.average_rating
        calculate_price = round(calc_price / self.distance_from_city_center, 1)
        return calculate_price

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power >= car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, single_rate: float) -> None:
        rating = self.average_rating * self.count_of_ratings + single_rate
        total_ratings = self.count_of_ratings + 1
        self.average_rating = round(rating / total_ratings, 1)
        self.count_of_ratings = total_ratings

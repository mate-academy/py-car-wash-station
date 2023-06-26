class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: float,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0.0

        for car in cars:
            if self.wash_single_car(car):
                income = self.calculate_washing_price(car)
                total_income += income
                car.clean_mark = self.clean_power

        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        difference = self.clean_power - car.clean_mark
        price = (car.comfort_class
                 * difference * self.average_rating
                 / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> bool:
        if self.clean_power >= car.clean_mark:
            return True
        return False

    def rate_service(self, rating: float) -> None:
        self.count_of_ratings += 1
        self.average_rating = round(
            (self.average_rating * (self.count_of_ratings - 1) + rating)
            / self.count_of_ratings,
            1
        )

class Car:
    def __init__(self,
                 comfort_class: int,
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

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class
                     * abs(car.clean_mark - self.clean_power)
                     * self.average_rating / self.distance_from_city_center, 1)

    def serve_cars(self, cars: list[Car]) -> float:
        overall_income = 0
        for car in cars:
            new_income = self.calculate_washing_price(car) \
                if car.clean_mark < self.clean_power else 0
            if new_income > 0:
                self.wash_single_car(car)
            overall_income += new_income
        return overall_income

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power \
            if car.clean_mark < self.clean_power else car.clean_mark

    def rate_service(self, rating: float) -> None:
        new_rating = self.average_rating * self.count_of_ratings + rating
        self.count_of_ratings += 1
        self.average_rating = round(new_rating / self.count_of_ratings, 1)

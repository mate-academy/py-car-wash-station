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
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0.0
        for car in cars:
            income += self.wash_single_car(car)
        return round(income, 1)

    def _calculate_price(self, car: Car) -> float:
        return (car.comfort_class
                * (self.clean_power - car.clean_mark)
                * self.average_rating
                / self.distance_from_city_center)

    def calculate_washing_price(self, car: Car) -> float:
        if self.clean_power > car.clean_mark:
            return round(self._calculate_price(car), 1)
        return 0.0

    def wash_single_car(self, car: Car) -> float:
        cost = 0.0
        if self.clean_power > car.clean_mark:
            cost = self._calculate_price(car)
            car.clean_mark = self.clean_power
        return cost

    def rate_service(self, rating: float) -> None:
        new_sum_rating = (self.average_rating * self.count_of_ratings) + rating
        self.count_of_ratings += 1
        self.average_rating = round(new_sum_rating / self.count_of_ratings, 1)

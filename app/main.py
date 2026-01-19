class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: float,
                 average_rating: float,
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                washing_price = self.calculate_washing_price(car)
                self.wash_single_car(car)
                income += washing_price
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        if self.clean_power <= car.clean_mark:
            return 0
        else:
            wash_cost = (car.comfort_class
                         * (self.clean_power - car.clean_mark)
                         * (self.average_rating
                            / self.distance_from_city_center))
            return wash_cost

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
        return

    def rate_service(self, rate: float) -> float:
        self.count_of_ratings += 1
        self.average_rating = round((((self.average_rating
                                       * (self.count_of_ratings - 1))
                                      + rate) / self.count_of_ratings), 1)
        return self.average_rating

class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        price = 0
        for each_car in cars:
            if each_car.clean_mark < self.clean_power:
                price += round(self.calculate_washing_price(each_car), 1)
                self.wash_single_car(each_car)
        return price

    def calculate_washing_price(self, car: Car) -> float:
        price = round(
            (car.comfort_class * (self.clean_power - car.clean_mark)
             * self.average_rating / self.distance_from_city_center), 1
        )
        return price

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, single_feedback: float) -> None:
        if single_feedback >= 0:
            self.count_of_ratings += 1
            self.average_rating = round(
                (self.average_rating * (self.count_of_ratings - 1)
                 + single_feedback) / self.count_of_ratings, 1
            )

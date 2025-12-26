class Car:
    def __init__(
            self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self, distance_from_city_center: float, clean_power: int,
            average_rating: float, count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        cars_to_wash = [
            car for car in cars if car.clean_mark < self.clean_power
        ]
        income = self.calculate_washing_price(cars_to_wash)
        self.wash_single_car(cars_to_wash)
        return income

    def calculate_washing_price(self, cars: list) -> float:
        if not isinstance(cars, list):
            cars = [cars]
        sum_ = 0
        for car in cars:
            sum_ += round(car.comfort_class
                          * (self.clean_power - car.clean_mark)
                          * self.average_rating
                          / self.distance_from_city_center, 1)
        return sum_

    def wash_single_car(self, cars: list) -> None:
        for car in cars:
            if car.clean_mark < self.clean_power:
                car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        self.average_rating = round(((self.average_rating
                                      * self.count_of_ratings) + rate)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

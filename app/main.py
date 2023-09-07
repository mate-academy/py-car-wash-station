class Car:

    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self, distance_from_city_center: int, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clear_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars_of_clients: list) -> float:
        income = 0
        for car1 in cars_of_clients:
            if self.wash_single_car(car1):
                car = car1
                income += self.calculate_washing_price(car1)
                car.clean_mark = self.clear_power
        return income

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class * (self.clear_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 1)

    def rate_service(self, rate: int) -> None:
        self.count_of_ratings += 1
        self.average_rating = round((self.average_rating
                                     * (self.count_of_ratings - 1) + rate)
                                    / self.count_of_ratings, 1)
        return

    def wash_single_car(self, car: Car) -> bool:
        if self.clear_power > car.clean_mark:
            return True

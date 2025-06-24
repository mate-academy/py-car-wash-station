class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int):
        if distance_from_city_center < 1.0:
            distance_from_city_center = 1.0
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        rate = self.average_rating * self.count_of_ratings + rate
        self.average_rating = round(rate / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

    def calculate_washing_price(self, car: Car) -> float:
        clean_difference = self.clean_power - car.clean_mark
        if clean_difference <= 0:
            return 0
        total = car.comfort_class * clean_difference * self.average_rating
        return round(total / round(self.distance_from_city_center, 1), 1)

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return round(income, 1)

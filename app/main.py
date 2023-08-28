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

    def serve_cars(self, cars: list) -> int:
        income = 0
        for car in cars:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        clean = self.clean_power - car.clean_mark
        if clean <= 0:
            return 0
        dist = self.distance_from_city_center
        return round(car.comfort_class * clean * self.average_rating / dist, 1)

    def wash_single_car(self, car: Car) -> None:
        clean = self.clean_power - car.clean_mark
        if clean > 0:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        all_rates = self.count_of_ratings * self.average_rating + rate
        self.average_rating = round(all_rates / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

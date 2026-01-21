class Car:
    def __init__(self,
                 comfort_class: float,
                 clean_mark: float,
                 brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: int,
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        comfort_class = car.comfort_class
        clean_diff = self.clean_power - car.clean_mark
        rating = self.average_rating
        distance = self.distance_from_city_center
        return round((comfort_class * clean_diff * rating / distance), 1)

    def wash_single_car(self, car: Car) -> None:
        if isinstance(car, Car):
            car.clean_mark = self.clean_power

    def is_wash_cars_possible(self, cars: list[Car]) -> list[Car]:
        return [car for car in cars if self.clean_power > car.clean_mark]

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        washed_cars = self.is_wash_cars_possible(cars)
        for car in washed_cars:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return income

    def rate_service(self, rate: float) -> None:
        total_rating = self.count_of_ratings * self.average_rating
        self.count_of_ratings += 1
        self.average_rating = (total_rating + rate) / self.count_of_ratings
        self.average_rating = round(self.average_rating, 1)

class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int,
                 clean_power: int, average_rating: int,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, serve_cars: list[Car]) -> float:
        total = 0
        for car in serve_cars:
            if car.clean_mark < self.clean_power:
                res = self.calculate_washing_price(car)
                total += res
                self.wash_single_car(car)
        return round(total, 1)

    def calculate_washing_price(self, car: Car) -> float:
        cost = (car.comfort_class * (self.clean_power - car.clean_mark)
                * (self.average_rating / self.distance_from_city_center))
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, single_rate: int) -> None:
        together = (self.average_rating * self.count_of_ratings) + single_rate
        self.count_of_ratings += 1
        self.average_rating = together / self.count_of_ratings
        self.average_rating = round(self.average_rating, 1)

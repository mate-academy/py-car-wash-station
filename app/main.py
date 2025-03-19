class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car: list[Car]) -> float:
        income = 0
        for cars in car:
            if cars.clean_mark < self.clean_power:
                income += self.calculate_washing_price(cars)
                self.wash_single_car(cars)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        res = (car.comfort_class
               * (self.clean_power - car.clean_mark)
               * self.average_rating
               / self.distance_from_city_center)
        return round(res, 1)

    def wash_single_car(self, car: Car) -> int:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
        return car.clean_mark

    def rate_service(self, new_rating: float) -> float:
        self.count_of_ratings += 1
        self.average_rating = ((self.average_rating
                                * (self.count_of_ratings - 1))
                               + new_rating) / self.count_of_ratings
        self.average_rating = round(self.average_rating, 1)
        return self.average_rating

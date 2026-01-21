class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_cars: list[Car]) -> list:
        result = 0
        for ready_car in [car for car in list_of_cars
                          if car.clean_mark <= self.clean_power]:
            result += self.calculate_washing_price(ready_car)
            ready_car.clean_mark = self.wash_single_car(ready_car)
        return round(result, 1)

    def calculate_washing_price(self, car: Car) -> int:
        return (car.comfort_class * (self.clean_power - car.clean_mark)
                * self.average_rating / self.distance_from_city_center)

    def wash_single_car(self, car: Car) -> int:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        return car.clean_mark

    def rate_service(self, rate: int) -> None:
        self.count_of_ratings += 1
        self.average_rating = round((
            ((self.count_of_ratings - 1) * self.average_rating)
            + rate) / self.count_of_ratings, 1)

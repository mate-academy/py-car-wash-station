class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class * (
            self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center, 1)

    def serve_cars(self, list_of_car: list[Car]) -> float:
        income_sum = 0
        for car in list_of_car:
            if car.clean_mark <= self.clean_power:
                income_one_car = round(self.calculate_washing_price(car), 1)
                income_sum += income_one_car
                self.wash_single_car(car)
        return income_sum

    def wash_single_car(self, car: Car) -> int:
        if self.clean_power >= car.clean_mark:
            car.clean_mark = self.clean_power
        return car.clean_mark

    def rate_service(self, single_rate: int) -> int:
        old_rating = (self.average_rating * self.count_of_ratings
                      ) + single_rate
        self.count_of_ratings += 1
        self.average_rating = round(old_rating / self.count_of_ratings, 1)
        return self.count_of_ratings

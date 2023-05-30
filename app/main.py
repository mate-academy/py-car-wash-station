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

    def calculate_washing_price(self, car: Car) -> int:
        return round((car.comfort_class
                      * (self.clean_power - car.clean_mark)
                      * (self.average_rating
                          / self.distance_from_city_center)), 1)

    def wash_single_car(self, car: Car) -> int:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
        return car.clean_mark

    def rate_service(self, rate: int) -> float:
        self.count_of_ratings += 1
        self.average_rating = round((
            ((self.count_of_ratings - 1)
             * self.average_rating
             + rate)
            / self.count_of_ratings), 1)
        return self.average_rating

    def serve_cars(self, cars_list: list[Car]) -> float:
        total_income = 0
        for car in cars_list:
            if self.calculate_washing_price(car) > 0:
                total_income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return total_income

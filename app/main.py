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

    def serve_cars(self, cars_list: list[Car]) -> float:
        income = 0
        for car in cars_list:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        dif_mark_power = self.clean_power - car.clean_mark
        multiply = car.comfort_class * (dif_mark_power) * self.average_rating
        result = multiply / self.distance_from_city_center
        return round(result, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        if 1.0 <= rate <= 5.0:
            self.count_of_ratings += 1
            calc = (self.average_rating * (self.count_of_ratings - 1) + rate)
            self.average_rating = round((calc / self.count_of_ratings), 1)

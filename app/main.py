class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        if comfort_class in list(range(1, 8)):
            self.comfort_class = comfort_class
        if clean_mark in list(range(1, 11)):
            self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        if 1.0 <= distance_from_city_center <= 10.0:
            self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        if 1.0 <= average_rating <= 5.0:
            self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        cleaning_difficulty = self.clean_power - car.clean_mark
        single_cleaning_price = (
            car.comfort_class * cleaning_difficulty
            * self.average_rating / self.distance_from_city_center
        )
        return round(single_cleaning_price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: int | float) -> None:
        sum_of_rates = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(sum_of_rates / self.count_of_ratings, 1)

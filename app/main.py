class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: list[Car]) -> float:
        income = 0
        for car in car_list:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        income = 0
        if car.clean_mark < self.clean_power:
            income = car.comfort_class * (self.clean_power - car.clean_mark)
            income *= self.average_rating / self.distance_from_city_center
        return round(income, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, grade: float) -> None:
        sum_grades = self.average_rating * self.count_of_ratings + grade
        self.count_of_ratings += 1
        self.average_rating = round(sum_grades / self.count_of_ratings, 1)

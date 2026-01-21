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

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        if self.clean_power > car.clean_mark:
            clean_comfort_correction = (car.comfort_class
                                        * (self.clean_power - car.clean_mark))
            rate_distance_ratio = (self.average_rating
                                   / self.distance_from_city_center)
            return round((clean_comfort_correction * rate_distance_ratio), 1)

    def serve_cars(self, cars: list[Car]) -> float:
        total_price = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_price += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return total_price

    def rate_service(self, rate_mark: float) -> None:
        rate_marks_sum = (self.count_of_ratings
                          * self.average_rating
                          + rate_mark)
        self.count_of_ratings += 1
        self.average_rating = round((rate_marks_sum
                                     / self.count_of_ratings), 1)
